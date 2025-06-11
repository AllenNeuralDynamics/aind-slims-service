"""Tests methods in ecephys handler module"""

import pytest
from unittest.mock import MagicMock
from typing import List
from aind_slims_service_server.handlers.ecephys import (
    EcephysSessionHandler,
)
from aind_slims_service_server.models import SlimsEcephysData


class TestEcephysSessionHandler:
    """Tests methods in EcephysSessionHandler class"""

    def test_get_graph(self, mock_get_ecephys_data: MagicMock):
        """Tests _get_graph method"""
        handler = EcephysSessionHandler(
            session=MagicMock(fetch=mock_get_ecephys_data)
        )
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

    def test_parse_graph(
        self,
        mock_get_ecephys_data: MagicMock,
        test_ecephys_data: List[SlimsEcephysData],
    ):
        """Tests _parse_graph method."""
        handler = EcephysSessionHandler(
            session=MagicMock(fetch=mock_get_ecephys_data)
        )
        g, root_nodes = handler._get_graph()
        ecephys_data = handler._parse_graph(
            g=g, root_nodes=root_nodes, subject_id="750108", session_name=None
        )
        assert test_ecephys_data == ecephys_data

    def test_get_ephys_data_from_slims(self, mock_get_ecephys_data):
        """Tests get_ephys_data_from_slims method"""
        handler = EcephysSessionHandler(
            session=MagicMock(fetch=mock_get_ecephys_data)
        )
        ecephys_data = handler.get_ephys_data_from_slims(subject_id="750108")
        assert len(ecephys_data) == 1

    def test_get_ephys_data_from_slims_error(self, mock_get_ecephys_data):
        """Tests get_ephys_data_from_slims method when subject_id empty"""
        handler = EcephysSessionHandler(
            session=MagicMock(fetch=mock_get_ecephys_data)
        )
        with pytest.raises(ValueError) as e:
            handler.get_ephys_data_from_slims(subject_id="")
        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
