"""
Module to handle fetching histology data from slims and parsing it to a model
"""

from datetime import datetime, timezone
from typing import List, Optional, Tuple

from networkx import DiGraph
from slims.criteria import is_one_of
from slims.internal import Record

from aind_slims_service_server.handlers.table_handler import (
    SlimsTableHandler,
)
from aind_slims_service_server.models import (
    HistologyReagentData,
    HistologyWashData,
    SlimsHistologyData,
)


class HistologySessionHandler(SlimsTableHandler):
    """Class to handle getting SPIM Histology Procedures info from SLIMS."""

    def _get_reagent_data(
        self, records: List[Record]
    ) -> List[HistologyReagentData]:
        """
        Get reagent data from records
        Parameters
        ----------
        records : List[Record]

        Returns
        -------
        List[HistologyReagentData]

        """

        reagents = []

        for record in records:
            if record.table_name() == "Content" and self.get_attr_or_none(
                record, "cntn_fk_category", "displayValue"
            ) in [
                "Reagents, Externally Manufactured",
                "Reagents, Internally Produced",
            ]:
                n_reagent_lot_number = self.get_attr_or_none(
                    record, "cntn_cf_lotNumber"
                )
                n_reagent_name = self.get_attr_or_none(
                    record, "cntn_cf_fk_catalogNumberReagents", "displayValue"
                )
                n_reagent_source = self.get_attr_or_none(
                    record, "cntn_fk_source", "displayValue"
                )
                reagent_data = HistologyReagentData(
                    name=n_reagent_name,
                    source=n_reagent_source,
                    lot_number=n_reagent_lot_number,
                )
                reagents.append(reagent_data)
        return reagents

    def _get_wash_data(
        self, g: DiGraph, exp_run_step: str, exp_run_step_row: Record
    ) -> HistologyWashData:
        """
        Get wash data from SLIMS records.
        Parameters
        ----------
        g : DiGraph
        exp_run_step : str
          Name of the node for the experiment run step
        exp_run_step_row : Record
          The Record attached to the node.

        Returns
        -------
        HistologyWashData

        """
        wash_data = HistologyWashData()
        wash_data.wash_name = self.get_attr_or_none(
            exp_run_step_row, "xprs_name"
        )
        wash_data.wash_type = self.get_attr_or_none(
            exp_run_step_row, "xprs_cf_spimWashType"
        )
        start_time_ts = self.get_attr_or_none(
            exp_run_step_row, "xprs_cf_startTime"
        )
        wash_data.start_time = (
            None
            if start_time_ts is None
            else datetime.fromtimestamp(start_time_ts / 1000, tz=timezone.utc)
        )
        end_time_ts = self.get_attr_or_none(
            exp_run_step_row, "xprs_cf_endTime"
        )
        wash_data.end_time = (
            None
            if end_time_ts is None
            else datetime.fromtimestamp(end_time_ts / 1000, tz=timezone.utc)
        )
        wash_data.modified_by = self.get_attr_or_none(
            exp_run_step_row, "xprs_modifiedBy"
        )
        wash_data.mass = self.get_attr_or_none(
            exp_run_step_row, "xprs_cf_mass"
        )
        wash_data_successors = g.successors(exp_run_step)
        records = [g.nodes[n]["row"] for n in wash_data_successors]
        reagents = self._get_reagent_data(records)
        wash_data.reagents = reagents
        return wash_data

    def _get_specimen_data(
        self, g: DiGraph, exp_run_step_content: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Get subject_id and specimen_id from Content record.
        Parameters
        ----------
        g : DiGraph
        exp_run_step_content : str
          Name of the node for the experiment run step content

        Returns
        -------
        tuple
          (subject_id, specimen_id)

        """
        content_nodes = g.successors(exp_run_step_content)
        records = [g.nodes[c]["row"] for c in content_nodes]
        specimen_id = None
        subject_id = None
        for record in records:
            n_subject_id = self.get_attr_or_none(record, "cntn_id")
            if n_subject_id is not None:
                subject_id = n_subject_id
            n_specimen_id = self.get_attr_or_none(record, "cntn_barCode")
            if n_specimen_id is not None:
                specimen_id = n_specimen_id
        return subject_id, specimen_id

    def _parse_graph(
        self, g: DiGraph, root_nodes: List[str], subject_id: Optional[str]
    ) -> List[SlimsHistologyData]:
        """
        Parses the graph object into a list of pydantic models.
        Parameters
        ----------
        g : DiGraph
          Graph of the SLIMS records.
        root_nodes : List[str]
          List of root nodes to pull descendants from.
        subject_id : str | None
          Labtracks ID of mouse to filter records by.

        Returns
        -------
        List[SlimsHistologyData]
        """

        histology_data_list = []
        for node in root_nodes:
            histology_data = SlimsHistologyData()
            washes = []
            experiment_run_created_on_ts = self.get_attr_or_none(
                g.nodes[node]["row"], "xprn_createdOn"
            )
            histology_data.experiment_run_created_on = (
                None
                if experiment_run_created_on_ts is None
                else datetime.fromtimestamp(
                    experiment_run_created_on_ts / 1000, tz=timezone.utc
                )
            )
            exp_run_name = self.get_attr_or_none(
                g.nodes[node]["row"], "xptm_name"
            )
            histology_data.procedure_name = exp_run_name

            exp_run_steps = g.successors(node)

            for exp_run_step in exp_run_steps:
                exp_run_step_row = g.nodes[exp_run_step]["row"]
                exp_run_step_name = self.get_attr_or_none(
                    exp_run_step_row, "xprs_name"
                )
                if exp_run_step_name in [
                    "Wash 1",
                    "Wash 2",
                    "Wash 3",
                    "Wash 4",
                    "Refractive Index Matching Wash",
                    "Primary Antibody Wash",
                    "Secondary Antibody Wash",
                    "MBS Wash",
                    "Gelation PBS Wash",
                    "Stock X + VA-044 Equilibration",
                    "Gelation + ProK RT",
                    "Gelation + Add'l ProK 37C",
                    "Final PBS Wash",
                ]:
                    wash_data = self._get_wash_data(
                        g,
                        exp_run_step=exp_run_step,
                        exp_run_step_row=exp_run_step_row,
                    )
                    washes.append(wash_data)

                exp_run_step_children = g.successors(exp_run_step)
                for exp_run_step_child in exp_run_step_children:
                    table_name = g.nodes[exp_run_step_child]["table_name"]
                    row = g.nodes[exp_run_step_child]["row"]
                    if table_name == "SOP":
                        stop_link = self.get_attr_or_none(row, "stop_link")
                        stop_name = self.get_attr_or_none(row, "stop_name")
                        histology_data.protocol_id = stop_link
                        histology_data.protocol_name = stop_name
                    if table_name == "ExperimentRunStepContent":
                        n_subject_id, n_specimen_id = self._get_specimen_data(
                            g=g, exp_run_step_content=exp_run_step_child
                        )
                        if n_subject_id is not None:
                            histology_data.subject_id = n_subject_id
                        if n_specimen_id is not None:
                            histology_data.specimen_id = n_specimen_id
            histology_data.washes = washes
            if subject_id is None or subject_id == histology_data.subject_id:
                histology_data_list.append(histology_data)
        return histology_data_list

    def _get_graph(
        self,
        start_date_greater_than_or_equal: Optional[datetime] = None,
        end_date_less_than_or_equal: Optional[datetime] = None,
    ) -> Tuple[DiGraph, List[str]]:
        """
        Generate a Graph of the records from SLIMS for histology.

        Parameters
        ----------
        start_date_greater_than_or_equal : datetime | None
          Filter experiment runs that were created on or after this datetime.
        end_date_less_than_or_equal : datetime | None
          Filter experiment runs that were created on or before this datetime.

        Returns
        -------
        Tuple[DiGraph, List[str]]
          A directed graph of the SLIMS records and a list of the root nodes.

        """
        experiment_template_rows = self.session.fetch(
            table="ExperimentTemplate",
            criteria=is_one_of(
                "xptm_name",
                [
                    "SmartSPIM Labeling",
                    "SmartSPIM Delipidation",
                    "SmartSPIM Refractive Index Matching",
                ],
            ),
        )
        date_criteria = self._get_date_criteria(
            start_date=start_date_greater_than_or_equal,
            end_date=end_date_less_than_or_equal,
            field_name="xprn_createdOn",
        )
        exp_run_rows = self.get_rows_from_foreign_table(
            input_table="ExperimentTemplate",
            input_rows=experiment_template_rows,
            input_table_cols=["xptm_pk"],
            foreign_table="ExperimentRun",
            foreign_table_col="xprn_fk_experimentTemplate",
            extra_criteria=date_criteria,
        )
        G = DiGraph()
        root_nodes = []
        for row in exp_run_rows:
            G.add_node(
                f"{row.table_name()}.{row.pk()}",
                row=row,
                pk=row.pk(),
                table_name=row.table_name(),
            )
            root_nodes.append(f"{row.table_name()}.{row.pk()}")

        exp_run_step_rows = self.get_rows_from_foreign_table(
            input_table="ExperimentRun",
            input_rows=exp_run_rows,
            input_table_cols=["xprn_pk"],
            foreign_table="ExperimentRunStep",
            foreign_table_col="xprs_fk_experimentRun",
            graph=G,
        )
        _ = self.get_rows_from_foreign_table(
            input_table="ExperimentRunStep",
            input_rows=exp_run_step_rows,
            input_table_cols=["xprs_cf_fk_protocol"],
            foreign_table="SOP",
            foreign_table_col="stop_pk",
            graph=G,
        )
        exp_run_step_content_rows = self.get_rows_from_foreign_table(
            input_table="ExperimentRunStep",
            input_rows=exp_run_step_rows,
            input_table_cols=["xprs_pk"],
            foreign_table="ExperimentRunStepContent",
            foreign_table_col="xrsc_fk_experimentRunStep",
            graph=G,
        )
        _ = self.get_rows_from_foreign_table(
            input_table="ExperimentRunStepContent",
            input_rows=exp_run_step_content_rows,
            input_table_cols=["xrsc_fk_content"],
            foreign_table="Content",
            foreign_table_col="cntn_pk",
            graph=G,
        )
        reagent_content_rows = self.get_rows_from_foreign_table(
            input_table="ExperimentRunStep",
            input_rows=exp_run_step_rows,
            input_table_cols=["xprs_cf_fk_reagent"],
            foreign_table="Content",
            foreign_table_col="cntn_pk",
            graph=G,
        )
        _ = self.get_rows_from_foreign_table(
            input_table="Content",
            input_rows=reagent_content_rows,
            input_table_cols=["cntn_cf_fk_catalogNumberReagents"],
            foreign_table="ReferenceDataRecord",
            foreign_table_col="rdrc_pk",
            graph=G,
        )
        return G, root_nodes

    def get_histology_data_from_slims(
        self,
        subject_id: Optional[str] = None,
        start_date_greater_than_or_equal: Optional[str] = None,
        end_date_less_than_or_equal: Optional[str] = None,
    ) -> List[SlimsHistologyData]:
        """
        Get Histology data from SLIMS.

        Parameters
        ----------
        subject_id : str | None
          Labtracks ID of mouse. If None, then no filter will be performed.
        start_date_greater_than_or_equal : str | None
          Filter experiment runs that were created on or after this datetime.
        end_date_less_than_or_equal : str | None
          Filter experiment runs that were created on or before this datetime.


        Returns
        -------
        List[SlimsHistologyData]

        Raises
        ------
        ValueError
          The subject_id cannot be an empty string.

        """

        if subject_id is not None and len(subject_id) == 0:
            raise ValueError("subject_id must not be empty!")

        G, root_nodes = self._get_graph(
            start_date_greater_than_or_equal=self.parse_date(
                start_date_greater_than_or_equal
            ),
            end_date_less_than_or_equal=self.parse_date(
                end_date_less_than_or_equal
            ),
        )
        hist_data = self._parse_graph(
            g=G, root_nodes=root_nodes, subject_id=subject_id
        )

        return hist_data
