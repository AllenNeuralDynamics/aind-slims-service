"""Module to retrieve ephys data from SLIMS using session object."""

from decimal import Decimal
from datetime import datetime
from typing import List, Optional, Tuple
from networkx import DiGraph, descendants
from slims.criteria import equals
from aind_slims_service_server.handlers.table_handler import get_attr_or_none, SlimsTableHandler
from aind_slims_service_server.models import (
    ReferenceDataRecord,
    Content,
    ExperimentRunStep,
    ExperimentRun,
    Result,
    SlimsEcephysData,
    EcephysRewardSpouts,
    EcephysStreamModule,
)
from slims.internal import Record

class EcephysSessionHandler(SlimsTableHandler):
    """Class to handle getting Ephys Session info from SLIMS."""

    @staticmethod
    def _get_stream_module_data(row: Record) -> EcephysStreamModule:
        """Parses a stream module info from a SLIMS row."""
        alias = lambda field: ReferenceDataRecord.model_fields[field].alias
        arc_angle = get_attr_or_none(row, alias("arc_angle"))
        module_angle = get_attr_or_none(row, alias("module_angle"))
        rotation_angle = get_attr_or_none(row, alias("rotation_angle"))
        ccf_coordinate_ap = get_attr_or_none(row, alias("ccf_coordinates_ap"))
        ccf_coordinate_ml = get_attr_or_none(row, alias("ccf_coordinates_ml"))
        ccf_coordinate_dv = get_attr_or_none(row, alias("ccf_coordinates_dv"))
        bregma_target_ap = get_attr_or_none(row, alias("bregma_target_ap"))
        bregma_target_ml = get_attr_or_none(row, alias("bregma_target_ml"))
        bregma_target_dv = get_attr_or_none(row, alias("bregma_target_dv"))
        surface_z = get_attr_or_none(row, alias("surface_z"))
        manipulator_x = get_attr_or_none(row, alias("manipulator_x"))
        manipulator_y = get_attr_or_none(row, alias("manipulator_y"))
        manipulator_z = get_attr_or_none(row, alias("manipulator_z"))
        return EcephysStreamModule(
            implant_hole=get_attr_or_none(row, alias("implant_hole")),
            assembly_name=get_attr_or_none(row, alias("assembly_name")),
            probe_name=get_attr_or_none(row, alias("ephys_probe_name")),
            primary_target_structure=get_attr_or_none(
                row, alias("primary_targeted_structure"), "displayValue"
            ),
            secondary_target_structures=get_attr_or_none(
                row, alias("secondary_targeted_structures"), "displayValues"
            ),
            arc_angle=(None if arc_angle is None else Decimal(str(arc_angle))),
            module_angle=(None if module_angle is None else Decimal(str(module_angle))),
            rotation_angle=(None if rotation_angle is None else Decimal(str(rotation_angle))),
            coordinate_transform=get_attr_or_none(
                row, alias("coordinate_transform"), "displayValue"
            ),
            ccf_coordinate_ap=(None if ccf_coordinate_ap is None else Decimal(str(ccf_coordinate_ap))),
            ccf_coordinate_ml=(None if ccf_coordinate_ml is None else Decimal(str(ccf_coordinate_ml))),
            ccf_coordinate_dv=(None if ccf_coordinate_dv is None else Decimal(str(ccf_coordinate_dv))),
            ccf_coordinate_unit=get_attr_or_none(
                row, alias("ccf_coordinates_ap"), "unit"
            ),
            ccf_version=get_attr_or_none(row, alias("ccf_version")),
            bregma_target_ap=(None if bregma_target_ap is None else Decimal(str(bregma_target_ap))),
            bregma_target_ml=(None if bregma_target_ml is None else Decimal(str(bregma_target_ml))),
            bregma_target_dv=(None if bregma_target_dv is None else Decimal(str(bregma_target_dv))),
            bregma_target_unit=get_attr_or_none(
                row, alias("bregma_target_ap"), "unit"
            ),
            surface_z=(None if surface_z is None else Decimal(str(surface_z))),
            surface_z_unit=get_attr_or_none(row, alias("surface_z"), "unit"),
            manipulator_x=(None if manipulator_x is None else Decimal(str(manipulator_x))),
            manipulator_y=(None if manipulator_y is None else Decimal(str(manipulator_y))),
            manipulator_z=(None if manipulator_z is None else Decimal(str(manipulator_z))),
            manipulator_unit=get_attr_or_none(
                row, alias("manipulator_x"), "unit"
            ),
            dye=get_attr_or_none(row, alias("dye"), "displayValue"),
        )

    @staticmethod
    def _get_reward_spouts_data(row: Record) -> EcephysRewardSpouts:
        """Parses a reward spouts info from a SLIMS row."""
        alias = lambda field: ReferenceDataRecord.model_fields[field].alias
        return EcephysRewardSpouts(
            spout_side=get_attr_or_none(row, alias("spout_side")),
            starting_position=get_attr_or_none(row, alias("starting_position")),
            variable_position=get_attr_or_none(row, alias("variable_position")),
        )

    def _handle_content(self, ephys_data: SlimsEcephysData, row: Record):
        """Handles the content table."""
        ephys_data.subject_id = get_attr_or_none(row, Content.model_fields["name"].alias)
        # ephys_data.subject_id = get_attr_or_none(row, Content.model_fields["barcode"].alias)

    def _handle_experimentrunstep(
        self, ephys_data: SlimsEcephysData, row: Record
    ):
        """Handles the experiment run step table."""
        alias = lambda field: ExperimentRunStep.model_fields[field].alias
        if get_attr_or_none(row, alias("name")) != "Group of Sessions":
            return
        ephys_data.operator = get_attr_or_none(
            row, alias("operator_dynamic"), "joinedDisplayValue"
        )
        ephys_data.session_type = get_attr_or_none(row, alias("session_type_fixed"))
        ephys_data.mouse_platform_name = get_attr_or_none(
            row, alias("mouse_platform_name")
        )
        ephys_data.active_mouse_platform = get_attr_or_none(
            row, alias("active_mouse_platform")
        )
        ephys_data.instrument = get_attr_or_none(
            row, alias("instrument_dynamic"), "displayValue"
        )
        ephys_data.device_calibrations = get_attr_or_none(
            row, alias("device_calibrations")
        )

    def _handle_result(self, ephys_data: SlimsEcephysData, row: Record):
        """Handles the result table."""
        alias = lambda field: Result.model_fields[field].alias
        label = get_attr_or_none(row, "test_label")
        if label == "Mouse Session":
            ephys_data.session_name = get_attr_or_none(
                row, alias("session_name")
            )
            animal_weight_prior = get_attr_or_none(
                row, alias("animal_weight_prior")
            )
            ephys_data.animal_weight_prior = (
                None
                if animal_weight_prior is None
                else Decimal(str(animal_weight_prior))
            )
            animal_weight_after = get_attr_or_none(
                row, alias("animal_weight_post")
            )
            ephys_data.animal_weight_after = (
                None
                if animal_weight_after is None
                else Decimal(str(animal_weight_after))
            )
            ephys_data.animal_weight_unit = get_attr_or_none(
                row, alias("animal_weight_prior"), "unit"
            )
            reward_consumed = get_attr_or_none(
                row, alias("reward_consumed")
            )
            ephys_data.reward_consumed = (
                None
                if reward_consumed is None
                else Decimal(str(reward_consumed))
            )
            ephys_data.reward_consumed_unit = get_attr_or_none(
                row, alias("reward_consumed"), "unit"
            )
            ephys_data.link_to_stimulus_epoch_code = get_attr_or_none(
                row, alias("link_to_stimulus_epoch_code")
            )
            ephys_data.stimulus_epochs = get_attr_or_none(
                row, alias("stimulus_epochs")
            )

        elif label == "Streams":
            ephys_data.stream_modalities = get_attr_or_none(
                row, alias("stream_modalities_fixed")
            )
            ephys_data.daq_names = get_attr_or_none(row, alias("daq_names_fixed"))
            ephys_data.camera_names = get_attr_or_none(
                row, alias("camera_names_fixed")
            )

    def _handle_referencedatarecord(
        self, ephys_data: SlimsEcephysData, row: Record
    ):
        """Handles the reference data record table."""
        alias = lambda field: ReferenceDataRecord.model_fields[field].alias
        ref_type = get_attr_or_none(
            row, alias("reference_data"), "displayValue"
        )
        if ref_type == "Reward Delivery":
            ephys_data.reward_solution = get_attr_or_none(
                row, alias("reward_solution")
            )
            ephys_data.other_reward_solution = get_attr_or_none(
                row, alias("specify_reward_solution")
            )
        elif ref_type == "Reward Spouts":
            ephys_data.reward_spouts.append(self._get_reward_spouts_data(row))
        elif ref_type == "Dome Module":
            ephys_data.stream_modules.append(self._get_stream_module_data(row))

    def _parse_graph(
        self,
        g: DiGraph,
        root_nodes: List[str],
        subject_id: Optional[str],
        session_name: Optional[str],
    ) -> List[SlimsEcephysData]:
        """
        Parses the graph object into a list of pydantic models.
        Parameters
        ----------
        g : DiGraph
          Graph of the SLIMS records.
        root_nodes : List[str]
          List of root nodes to pull descendants from.
        subject_id : Optional[str]
          Labtracks ID of mouse to filter records by.
        session_name : Optional[str]
            Name of the session to filter records by.
        Returns
        -------
        List[SlimsEcephysData]
        """
        ephys_data_list = []

        for node in root_nodes:
            ephys_data = SlimsEcephysData()
            ephys_data.experiment_run_created_on = get_attr_or_none(
                g.nodes[node]["row"], ExperimentRun.model_fields["created_on"].alias
            )
            for n in descendants(g, node):
                row = g.nodes[n]["row"]
                table_name = g.nodes[n]["table_name"]

                table_handler = getattr(
                    self, f"_handle_{table_name.lower()}", None
                )
                if table_handler:
                    table_handler(ephys_data, row)
            if (
                subject_id is None or subject_id == ephys_data.subject_id
            ) and (
                session_name is None or session_name == ephys_data.session_name
            ):
                ephys_data_list.append(
                    SlimsEcephysData.model_validate(ephys_data.model_dump())
                )

        return ephys_data_list

    def _get_graph(
        self,
        start_date_greater_than_or_equal: Optional[datetime] = None,
        end_date_less_than_or_equal: Optional[datetime] = None,
    ) -> Tuple[DiGraph, List[str]]:
        """
        Generate a Graph of the records from SLIMS for Ecephys experiment runs.
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
            criteria=equals(
                "xptm_name", "In Vivo Electrophysiology Recording"
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
        exp_run_step_content_rows = self.get_rows_from_foreign_table(
            input_table="ExperimentRunStep",
            input_rows=exp_run_step_rows,
            input_table_cols=["xprs_pk"],
            foreign_table="ExperimentRunStepContent",
            foreign_table_col="xrsc_fk_experimentRunStep",
            graph=G,
        )
        result_rows = self.get_rows_from_foreign_table(
            input_table="ExperimentRunStep",
            input_rows=exp_run_step_rows,
            input_table_cols=["xprs_pk"],
            foreign_table="Result",
            foreign_table_col="rslt_fk_experimentRunStep",
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
        reference_data_rows = self.get_rows_from_foreign_table(
            input_table="Result",
            input_rows=result_rows,
            input_table_cols=[
                "rslt_cf_fk_modulesinStream",
                "rslt_cf_fk_rewardDelivery",
            ],
            foreign_table="ReferenceDataRecord",
            foreign_table_col="rdrc_pk",
            graph=G,
        )
        _ = self.get_rows_from_foreign_table(
            input_table="ReferenceDataRecord",
            input_rows=reference_data_rows,
            input_table_cols=["rdrc_cf_fk_rewardSpouts"],
            foreign_table="ReferenceDataRecord",
            foreign_table_col="rdrc_pk",
            graph=G,
        )

        return G, root_nodes

    def get_ephys_data_from_slims(
        self,
        subject_id: Optional[str] = None,
        session_name: Optional[str] = None,
        start_date_greater_than_or_equal: Optional[datetime] = None,
        end_date_less_than_or_equal: Optional[datetime] = None,
    ) -> List[SlimsEcephysData]:
        """
        Get Ephys data from SLIMS.

        Parameters
        ----------
        subject_id : str | None
          Labtracks ID of mouse. If None, then no filter will be performed.
        session_name : str | None
          Name of the session. If None, then no filter will be performed.
        start_date_greater_than_or_equal : datetime | None
          Filter experiment runs that were created on or after this datetime.
        end_date_less_than_or_equal : datetime | None
          Filter experiment runs that were created on or before this datetime.

        Returns
        -------
        List[SlimsSpimData]

        Raises
        ------
        ValueError
          The subject_id cannot be an empty string.

        """

        if subject_id is not None and len(subject_id) == 0:
            raise ValueError("subject_id must not be empty!")

        G, root_nodes = self._get_graph(
            start_date_greater_than_or_equal=start_date_greater_than_or_equal,
            end_date_less_than_or_equal=end_date_less_than_or_equal,
        )

        ephys_data = self._parse_graph(
            g=G,
            root_nodes=root_nodes,
            subject_id=subject_id,
            session_name=session_name,
        )

        ephys_data.sort(
            key=lambda m: (
                m.experiment_run_created_on is None,
                m.experiment_run_created_on,
            ),
            reverse=True,
        )

        return ephys_data
