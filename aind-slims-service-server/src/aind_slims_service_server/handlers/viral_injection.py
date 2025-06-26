"""
Module to handle fetching viral injection data from slims
and parsing it to a model.
"""

from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Optional, Tuple

from networkx import DiGraph, descendants
from slims.criteria import equals

from aind_slims_service_server.handlers.table_handler import (
    SlimsTableHandler,
)
from aind_slims_service_server.models import (
    SlimsViralInjectionData,
    SlimsViralMaterialData,
)


class ViralInjectionSessionHandler(SlimsTableHandler):
    """Class to handle getting Viral Injection info from SLIMS."""

    def _parse_graph(
        self, g: DiGraph, root_nodes: List[str], subject_id: Optional[str]
    ) -> List[SlimsViralInjectionData]:
        """
        Parses the graph object into a list of pydantic models.
        Parameters
        ----------
        g : DiGraph
          Graph of the SLIMS records.
        root_nodes : List[str]
          List of root nodes to pull descendants from.

        Returns
        -------
        List[SlimsViralInjectionData]

        """
        vi_data_list = []
        for node in root_nodes:
            vi_data = SlimsViralInjectionData()
            node_des = descendants(g, node)
            root_row = g.nodes[node]["row"]
            content_created_on_ts = self.get_attr_or_none(
                root_row, "cntn_createdOn"
            )
            vi_data.content_created_on = (
                None
                if content_created_on_ts is None
                else datetime.fromtimestamp(
                    content_created_on_ts / 1000, tz=timezone.utc
                )
            )
            vi_data.content_category = self.get_attr_or_none(
                root_row, "cntn_fk_category", "displayValue"
            )
            vi_data.content_type = self.get_attr_or_none(
                root_row, "cntn_fk_contentType", "displayValue"
            )
            vi_data.content_created_on = (
                None
                if content_created_on_ts is None
                else datetime.fromtimestamp(
                    content_created_on_ts / 1000, tz=timezone.utc
                )
            )
            content_modified_on_ts = self.get_attr_or_none(
                root_row, "cntn_modifiedOn"
            )
            vi_data.content_modified_on = (
                None
                if content_modified_on_ts is None
                else datetime.fromtimestamp(
                    content_modified_on_ts / 1000, tz=timezone.utc
                )
            )
            vi_data.viral_injection_buffer = self.get_attr_or_none(
                root_row, "cntn_cf_fk_viralInjectionBuffer", "displayValue"
            )
            volume = self.get_attr_or_none(root_row, "cntn_cf_volumeRequired")
            vi_data.volume = None if volume is None else Decimal(str(volume))
            vi_data.volume_unit = self.get_attr_or_none(
                root_row, "cntn_cf_volumeRequired", "unit"
            )
            vi_data.labeling_protein = self.get_attr_or_none(
                root_row,
                "cntn_cf_fk_viralInjectionFluorescentLabelingP",
                "displayValue",
            )
            vi_data.name = self.get_attr_or_none(root_row, "cntn_id")
            date_made_ts = self.get_attr_or_none(root_row, "cntn_cf_dateMade")
            vi_data.date_made = (
                None
                if date_made_ts is None
                else datetime.fromtimestamp(
                    date_made_ts / 1000, tz=timezone.utc
                )
            )
            intake_date_ts = self.get_attr_or_none(
                root_row, "cntn_cf_intakeDate_NA"
            )
            vi_data.intake_date = (
                None
                if intake_date_ts is None
                else datetime.fromtimestamp(
                    intake_date_ts / 1000, tz=timezone.utc
                )
            )
            vi_data.storage_temperature = self.get_attr_or_none(
                root_row, "cntn_cf_fk_storageTemp_dynChoice", "displayValue"
            )
            vi_data.special_storage_guidelines = self.get_attr_or_none(
                root_row,
                "cntn_cf_fk_specialStorageGuidelines",
                "displayValues",
            )
            vi_data.special_handling_guidelines = self.get_attr_or_none(
                root_row,
                "cntn_cf_fk_specialHandlingGuidelines",
                "displayValues",
            )
            for n in node_des:
                table_name = g.nodes[n]["table_name"]
                row = g.nodes[n]["row"]
                if table_name == "Order":
                    vi_data.assigned_mice = self.get_attr_or_none(
                        row, "ordr_cf_fk_assignedMice", "displayValues"
                    )
                    requested_for_date_ts = self.get_attr_or_none(
                        row, "ordr_cf_requestedForDate"
                    )
                    vi_data.requested_for_date = (
                        None
                        if requested_for_date_ts is None
                        else datetime.fromtimestamp(
                            requested_for_date_ts / 1000, tz=timezone.utc
                        )
                    )
                    planned_injection_date_ts = self.get_attr_or_none(
                        row, "ordr_plannedOnDate"
                    )
                    vi_data.planned_injection_date = (
                        None
                        if planned_injection_date_ts is None
                        else datetime.fromtimestamp(
                            planned_injection_date_ts / 1000, tz=timezone.utc
                        )
                    )
                    planned_injection_time_ts = self.get_attr_or_none(
                        row, "ordr_plannedOnTime"
                    )
                    vi_data.planned_injection_time = (
                        None
                        if planned_injection_time_ts is None
                        else datetime.fromtimestamp(
                            planned_injection_time_ts / 1000, tz=timezone.utc
                        )
                    )
                    order_created_on_ts = self.get_attr_or_none(
                        row, "ordr_createdOn"
                    )
                    vi_data.order_created_on = (
                        None
                        if order_created_on_ts is None
                        else datetime.fromtimestamp(
                            order_created_on_ts / 1000, tz=timezone.utc
                        )
                    )
                    vi_data.derivation_count = self.get_attr_or_none(
                        row, "derivedCount"
                    )
                    vi_data.ingredient_count = self.get_attr_or_none(
                        row, "ingredientCount"
                    )
                    vi_data.mix_count = self.get_attr_or_none(row, "mixCount")
                if (
                    table_name == "Content"
                    and self.get_attr_or_none(
                        row, "cntn_fk_contentType", "displayValue"
                    )
                    == "Viral solution"
                ):
                    vm_data = SlimsViralMaterialData()
                    vm_data.content_category = self.get_attr_or_none(
                        row, "cntn_fk_category", "displayValue"
                    )
                    vm_data.content_type = self.get_attr_or_none(
                        row, "cntn_fk_contentType", "displayValue"
                    )
                    content_created_on_ts = self.get_attr_or_none(
                        row, "cntn_createdOn"
                    )
                    vm_data.content_created_on = (
                        None
                        if content_created_on_ts is None
                        else datetime.fromtimestamp(
                            content_created_on_ts / 1000, tz=timezone.utc
                        )
                    )
                    content_modified_on_ts = self.get_attr_or_none(
                        row, "cntn_modifiedOn"
                    )
                    vm_data.content_modified_on = (
                        None
                        if content_modified_on_ts is None
                        else datetime.fromtimestamp(
                            content_modified_on_ts / 1000, tz=timezone.utc
                        )
                    )
                    vm_data.viral_solution_type = self.get_attr_or_none(
                        row, "cntn_cf_fk_viralSolutionType", "displayValue"
                    )
                    vm_data.virus_name = self.get_attr_or_none(
                        row, "cntn_cf_virusName"
                    )
                    vm_data.lot_number = self.get_attr_or_none(
                        row, "cntn_cf_lotNumber"
                    )
                    vm_data.lab_team = self.get_attr_or_none(
                        row, "cntn_cf_fk_labTeam", "displayValue"
                    )
                    vm_data.virus_type = self.get_attr_or_none(
                        row, "cntn_cf_fk_virusType", "displayValue"
                    )
                    vm_data.virus_serotype = self.get_attr_or_none(
                        row, "cntn_cf_fk_virusSerotype", "displayValue"
                    )
                    vm_data.virus_plasmid_number = self.get_attr_or_none(
                        row, "cntn_cf_virusPlasmidNumber"
                    )
                    vm_data.name = self.get_attr_or_none(row, "cntn_id")
                    dose = self.get_attr_or_none(row, "cntn_cf_dose")
                    vm_data.dose = None if dose is None else Decimal(str(dose))
                    vm_data.dose_unit = self.get_attr_or_none(
                        row, "cntn_cf_doseUnit", "unit"
                    )
                    titer = self.get_attr_or_none(row, "cntn_cf_titer")
                    vm_data.titer = (
                        None if titer is None else Decimal(str(titer))
                    )
                    vm_data.titer_unit = self.get_attr_or_none(
                        row, "cntn_cf_titer", "unit"
                    )
                    volume = self.get_attr_or_none(
                        row, "cntn_cf_volumeRequired"
                    )
                    vm_data.volume = (
                        None if volume is None else Decimal(str(volume))
                    )
                    vm_data.volume_unit = self.get_attr_or_none(
                        row, "cntn_cf_volumeRequired", "unit"
                    )
                    date_made_ts = self.get_attr_or_none(
                        row, "cntn_cf_dateMade"
                    )
                    vm_data.date_made = (
                        None
                        if date_made_ts is None
                        else datetime.fromtimestamp(
                            date_made_ts / 1000, tz=timezone.utc
                        )
                    )
                    intake_date_ts = self.get_attr_or_none(
                        row, "cntn_cf_intakeDate_NA"
                    )
                    vm_data.intake_date = (
                        None
                        if intake_date_ts is None
                        else datetime.fromtimestamp(
                            intake_date_ts / 1000, tz=timezone.utc
                        )
                    )
                    vm_data.storage_temperature = self.get_attr_or_none(
                        row, "cntn_cf_fk_storageTemp_dynChoice", "displayValue"
                    )
                    vm_data.special_storage_guidelines = self.get_attr_or_none(
                        row,
                        "cntn_cf_fk_specialStorageGuidelines",
                        "displayValues",
                    )
                    vm_data.special_handling_guidelines = (
                        self.get_attr_or_none(
                            row,
                            "cntn_cf_fk_specialHandlingGuidelines",
                            "displayValues",
                        )
                    )
                    vm_data.derivation_count = self.get_attr_or_none(
                        row, "derivedCount"
                    )
                    vm_data.ingredient_count = self.get_attr_or_none(
                        row, "ingredientCount"
                    )
                    vm_data.mix_count = self.get_attr_or_none(row, "mixCount")
                    vi_data.viral_materials.append(vm_data)
            if subject_id is None or subject_id in vi_data.assigned_mice:
                vi_data_list.append(vi_data)
        return vi_data_list

    def _get_graph(
        self,
        start_date_greater_than_or_equal: Optional[datetime] = None,
        end_date_less_than_or_equal: Optional[datetime] = None,
    ) -> Tuple[DiGraph, List[str]]:
        """
        Generate a Graph of the records from SLIMS for viral injection
        contents.
        Parameters
        ----------
        start_date_greater_than_or_equal : datetime | None
          The start date to filter the records by.
        end_date_less_than_or_equal : datetime | None
            The end date to filter the records by.
        Returns
        -------
        Tuple[DiGraph, List[str]]
          A directed graph of the SLIMS records and a list of the root nodes.

        """
        content_type_rows = self.session.fetch(
            table="ContentType",
            criteria=equals("cntp_name", "Viral Injection"),
        )
        date_criteria = self._get_date_criteria(
            start_date=start_date_greater_than_or_equal,
            end_date=end_date_less_than_or_equal,
            field_name="cntn_createdOn",
        )
        viral_injection_content_rows = self.get_rows_from_foreign_table(
            input_table="ContentType",
            input_rows=content_type_rows,
            input_table_cols=["cntp_pk"],
            foreign_table="Content",
            foreign_table_col="cntn_fk_contentType",
            extra_criteria=date_criteria,
        )
        G = DiGraph()
        root_nodes = []
        for row in viral_injection_content_rows:
            G.add_node(
                f"{row.table_name()}.{row.pk()}",
                row=row,
                pk=row.pk(),
                table_name=row.table_name(),
            )
            root_nodes.append(f"{row.table_name()}.{row.pk()}")

        # content relation: viral injection -> viral materials
        content_relation_rows = self.get_rows_from_foreign_table(
            input_table="Content",
            input_rows=viral_injection_content_rows,
            input_table_cols=["cntn_pk"],
            foreign_table="ContentRelation",
            foreign_table_col="corl_fk_to",
            graph=G,
        )
        _ = self.get_rows_from_foreign_table(
            input_table="ContentRelation",
            input_rows=content_relation_rows,
            input_table_cols=["corl_fk_from"],
            foreign_table="Content",
            foreign_table_col="cntn_pk",
            graph=G,
        )
        _ = self.get_rows_from_foreign_table(
            input_table="Content",
            input_rows=viral_injection_content_rows,
            input_table_cols=["cntn_pk"],
            foreign_table="Order",
            foreign_table_col="ordr_cf_fk_viralInjection",
            graph=G,
        )

        return G, root_nodes

    def get_viral_injection_info_from_slims(
        self,
        subject_id: Optional[str] = None,
        start_date_greater_than_or_equal: Optional[str] = None,
        end_date_less_than_or_equal: Optional[str] = None,
    ) -> List[SlimsViralInjectionData]:
        """
        Get Viral injection data from SLIMS.

        Parameters
        ----------
        subject_id : Optional[str]
            The subject ID to filter the data by.
            If None, all subjects are included.
        start_date_greater_than_or_equal : Optional[str]
            The start date to filter the data by, in ISO format (YYYY-MM-DD).
            If None, no start date filter is applied.
        end_date_less_than_or_equal : Optional[str]
            The end date to filter the data by, in ISO format (YYYY-MM-DD).
            If None, no end date filter is applied.
        Returns
        -------
        List[SlimsViralInjectionData]

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
        vm_data = self._parse_graph(
            g=G, root_nodes=root_nodes, subject_id=subject_id
        )
        return vm_data
