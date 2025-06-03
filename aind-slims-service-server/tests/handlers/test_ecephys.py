"""Tests methods in ecephys handler module"""

import json
import os
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict
import unittest
from unittest.mock import MagicMock, patch
import pytest
from slims.internal import Record

from aind_slims_service_server.handlers.ecephys import (
    SlimsEcephysData,
    EcephysSessionHandler,
    EcephysRewardSpouts,
    EcephysStreamModule,
)
from datetime import datetime, timezone

RESOURCES_DIR = (
    Path(os.path.dirname(os.path.realpath(__file__)))
    / ".."
    / "resources"
    / "ecephys"
)


@pytest.fixture(autouse=True)
def setup_ecephys_data(load_ecephys_json, form_record):
    content = [form_record(j) for j in load_ecephys_json("content.json")]
    experiment_run = [form_record(j) for j in load_ecephys_json("experiment_run.json")]
    experiment_run_step = [form_record(j) for j in load_ecephys_json("experiment_run_step.json")]
    experiment_run_step_content = [form_record(j) for j in load_ecephys_json("experiment_run_step_content.json")]
    experiment_template = [form_record(j) for j in load_ecephys_json("experiment_template.json")]
    reference_data_record = [form_record(j) for j in load_ecephys_json("reference_data_record.json")]
    result = [form_record(j) for j in load_ecephys_json("result.json")]

    return {
        "content": content,
        "experiment_run": experiment_run,
        "experiment_run_step": experiment_run_step,
        "experiment_run_step_content": experiment_run_step_content,
        "experiment_template": experiment_template,
        "reference_data_record": reference_data_record,
        "result": result,
    }


@pytest.fixture
def fetch_side_effect(setup_ecephys_data):
    """Provides the fetch_side_effect list for mocks."""
    return [
        setup_ecephys_data["experiment_template"],
        setup_ecephys_data["experiment_run"],
        setup_ecephys_data["experiment_run_step"],
        setup_ecephys_data["experiment_run_step_content"],
        setup_ecephys_data["result"],
        setup_ecephys_data["content"],
        setup_ecephys_data["reference_data_record"],
        setup_ecephys_data["reference_data_record"],
    ]


class TestEcephysSessionHandler:
    """Tests methods in EcephysSessionHandler class"""

    @patch("slims.slims.Slims")
    def test_get_graph(self, mock_slims: MagicMock, fetch_side_effect):
        """Tests _get_graph method"""

        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        G, root_nodes = handler._get_graph()
        expected_root_nodes = [
            "ExperimentRun.40007",
        ]
        expected_edges = [
            ("ExperimentRun.40007", "ExperimentRunStep.60027"),
            ("ExperimentRun.40007", "ExperimentRunStep.60028"),
            ("ExperimentRun.40007", "ExperimentRunStep.60029"),
            ("ExperimentRun.40007", "ExperimentRunStep.60030"),
            ("ExperimentRunStep.60027", "ExperimentRunStepContent.9"),
            ("ExperimentRunStep.60029", "Result.1581"),
            ("ExperimentRunStep.60030", "Result.1611"),
            ("ExperimentRunStepContent.9", "Content.166"),
            ("Result.1581", "ReferenceDataRecord.3466"),
            ("Result.1611", "ReferenceDataRecord.4512"),
            ("ReferenceDataRecord.3466", "ReferenceDataRecord.3467"),
        ]
        assert expected_root_nodes == root_nodes
        assert set(expected_edges) == set(G.edges())

    @patch("slims.slims.Slims")
    def test_parse_graph(self, mock_slims: MagicMock, fetch_side_effect):
        """Tests _parse_graph method."""
        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        g, root_nodes = handler._get_graph()
        ecephys_data = handler._parse_graph(
            g=g, root_nodes=root_nodes, subject_id="750108", session_name=None
        )
        expected_ecephys_data = [
            SlimsEcephysData(
                experiment_run_created_on=datetime(2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc),
                subject_id="750108",
                operator="Person Merson",
                instrument=None,
                session_type="Dynamic Foraging",
                device_calibrations=None,
                mouse_platform_name="Dynamic Foraging",
                active_mouse_platform=True,
                session_name="ecephys_750108_2024-12-23_14-51-45",
                animal_weight_prior=Decimal("30.2"),
                animal_weight_after=Decimal("30.5"),
                animal_weight_unit="g",
                reward_consumed=Decimal("1"),
                reward_consumed_unit="ml",
                stimulus_epochs=410,
                link_to_stimulus_epoch_code=("git@github.com:SomeLink.git"),
                reward_solution="Water",
                other_reward_solution=None,
                reward_spouts=[
                    EcephysRewardSpouts(
                        spout_side="Water",
                        starting_position=None,
                        variable_position=None,
                    )
                ],
                stream_modalities=["Behavior", "Behavior Videos", "Ecephys"],
                stream_modules=[
                    EcephysStreamModule(
                        implant_hole=5,
                        assembly_name="50209",
                        probe_name="50209",
                        primary_target_structure="Retrosplenial area",
                        secondary_target_structures=None,
                        arc_angle=Decimal("-17.0"),
                        module_angle=Decimal("12.0"),
                        rotation_angle=Decimal("0.0"),
                        coordinate_transform=(
                            "calibration_info_np2_2024_12_23T11_36_00.xlsx"
                        ),
                        ccf_coordinate_ap=Decimal("0.5"),
                        ccf_coordinate_ml=Decimal("0.5"),
                        ccf_coordinate_dv=Decimal("0.5"),
                        ccf_coordinate_unit="&mu;m",
                        ccf_version=None,
                        bregma_target_ap=Decimal("0.5"),
                        bregma_target_ml=Decimal("0.5"),
                        bregma_target_dv=Decimal("0.5"),
                        bregma_target_unit="mm",
                        surface_z=Decimal("5508.5"),
                        surface_z_unit="&mu;m",
                        manipulator_x=Decimal("7610.0"),
                        manipulator_y=Decimal("9063.0"),
                        manipulator_z=Decimal("6703.0"),
                        manipulator_unit="&mu;m",
                        dye="DiI",
                    )
                ],
                daq_names=["Basestation Slot 3"],
                camera_names=[
                    "Bottom camera",
                    "Eye camera",
                    "Side camera left",
                ],
            )
        ]
        assert expected_ecephys_data == ecephys_data

    @patch("slims.slims.Slims")
    def test_get_ephys_data_from_slims(self, mock_slims: MagicMock, fetch_side_effect):
        """Tests get_ephys_data_from_slims method"""
        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        ecephys_data = handler.get_ephys_data_from_slims(subject_id="750108")
        assert len(ecephys_data) == 1

    @patch("slims.slims.Slims")
    def test_get_ephys_data_from_slims_error(self, mock_slims: MagicMock, fetch_side_effect):
        """Tests get_ephys_data_from_slims method when subject_id empty"""
        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        with pytest.raises(ValueError) as e:
            handler.get_ephys_data_from_slims(subject_id="")

        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    unittest.main()