"""Tests methods in ecephys handler module"""

from unittest.mock import MagicMock, patch

import pytest

from aind_slims_service_server.handlers.ecephys import (
    EcephysSessionHandler,
)


@pytest.fixture(autouse=True)
def setup_ecephys_data(load_json, form_record):
    """Fixture to set up ecephys data for tests."""
    content = [form_record(j) for j in load_json("content.json", subdir="ecephys")]
    experiment_run = [
        form_record(j) for j in load_json("experiment_run.json", subdir="ecephys")
    ]
    experiment_run_step = [
        form_record(j) for j in load_json("experiment_run_step.json", subdir="ecephys")
    ]
    experiment_run_step_content = [
        form_record(j)
        for j in load_json("experiment_run_step_content.json", subdir="ecephys")
    ]
    experiment_template = [
        form_record(j) for j in load_json("experiment_template.json", subdir="ecephys")
    ]
    reference_data_record = [
        form_record(j) for j in load_json("reference_data_record.json", subdir="ecephys")
    ]
    result = [form_record(j) for j in load_json("result.json", subdir="ecephys")]

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
    def test_parse_graph(
        self, mock_slims: MagicMock, fetch_side_effect, test_ecephys_data
    ):
        """Tests _parse_graph method."""
        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        g, root_nodes = handler._get_graph()
        ecephys_data = handler._parse_graph(
            g=g, root_nodes=root_nodes, subject_id="750108", session_name=None
        )
        assert test_ecephys_data == ecephys_data

    @patch("slims.slims.Slims")
    def test_get_ephys_data_from_slims(
        self, mock_slims: MagicMock, fetch_side_effect
    ):
        """Tests get_ephys_data_from_slims method"""
        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        ecephys_data = handler.get_ephys_data_from_slims(subject_id="750108")
        assert len(ecephys_data) == 1

    @patch("slims.slims.Slims")
    def test_get_ephys_data_from_slims_error(
        self, mock_slims: MagicMock, fetch_side_effect
    ):
        """Tests get_ephys_data_from_slims method when subject_id empty"""
        mock_slims.fetch.side_effect = fetch_side_effect
        handler = EcephysSessionHandler(session=mock_slims)
        with pytest.raises(ValueError) as e:
            handler.get_ephys_data_from_slims(subject_id="")

        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
