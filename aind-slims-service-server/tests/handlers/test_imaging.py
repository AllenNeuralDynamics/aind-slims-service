"""Tests methods in ssmartspim imaging handler module"""

from typing import List
from unittest.mock import MagicMock
import pytest
from aind_slims_service_server.handlers.imaging import (
    ImagingSessionHandler,
)
from aind_slims_service_server.models import SlimsSpimData


class TestImagingSessionHandler:
    """Tests methods in ImagingSessionHandler class"""

    def test_get_graph(self, mock_get_imaging_data: MagicMock):
        """Tests _get_graph method"""

        handler = ImagingSessionHandler(
            session=MagicMock(fetch=mock_get_imaging_data)
        )
        G, root_nodes = handler._get_graph()
        expected_root_nodes = [
            "ExperimentRun.40015",
            "ExperimentRun.40016",
            "ExperimentRun.40017",
        ]
        expected_edges = [
            ("ExperimentRun.40015", "ExperimentRunStep.60059"),
            ("ExperimentRun.40015", "ExperimentRunStep.60060"),
            ("ExperimentRun.40015", "ExperimentRunStep.60061"),
            ("ExperimentRun.40016", "ExperimentRunStep.60062"),
            ("ExperimentRun.40016", "ExperimentRunStep.60063"),
            ("ExperimentRun.40016", "ExperimentRunStep.60064"),
            ("ExperimentRun.40017", "ExperimentRunStep.60065"),
            ("ExperimentRun.40017", "ExperimentRunStep.60066"),
            ("ExperimentRun.40017", "ExperimentRunStep.60067"),
            ("ExperimentRunStep.60059", "ExperimentRunStepContent.29"),
            ("ExperimentRunStep.60060", "Result.1581"),
            ("ExperimentRunStep.60061", "SOP.18"),
            ("ExperimentRunStep.60062", "ExperimentRunStepContent.30"),
            ("ExperimentRunStep.60063", "Result.1611"),
            ("ExperimentRunStep.60064", "SOP.18"),
            ("ExperimentRunStep.60065", "ExperimentRunStepContent.31"),
            ("ExperimentRunStep.60066", "Result.1644"),
            ("ExperimentRunStep.60067", "SOP.18"),
            ("ExperimentRunStepContent.29", "Content.233"),
            ("ExperimentRunStepContent.30", "Content.235"),
            ("ExperimentRunStepContent.31", "Content.234"),
            ("Result.1581", "ReferenceDataRecord.40"),
            ("Result.1581", "ReferenceDataRecord.1624"),
            ("Result.1611", "ReferenceDataRecord.40"),
            ("Result.1611", "ReferenceDataRecord.1624"),
            ("Result.1644", "ReferenceDataRecord.40"),
            ("Result.1644", "ReferenceDataRecord.1624"),
            ("Content.235", "OrderContent.32"),
            ("OrderContent.32", "Order.21"),
        ]
        assert expected_root_nodes == root_nodes
        assert set(expected_edges) == set(G.edges())

    def test_parse_graph(
        self,
        mock_get_imaging_data: MagicMock,
        test_imaging_data: List[SlimsSpimData],
    ):
        """Tests _parse_graph method."""
        handler = ImagingSessionHandler(
            session=MagicMock(fetch=mock_get_imaging_data)
        )
        g, root_nodes = handler._get_graph()
        spim_data = handler._parse_graph(
            g=g, root_nodes=root_nodes, subject_id="744742"
        )
        assert test_imaging_data == spim_data

    def test_get_spim_data_from_slims(self, mock_get_imaging_data: MagicMock):
        """Tests get_spim_data_from_slims method"""
        handler = ImagingSessionHandler(
            session=MagicMock(fetch=mock_get_imaging_data)
        )
        spim_data = handler.get_spim_data_from_slims(subject_id="744742")
        assert len(spim_data) == 1

    def test_get_spim_data_from_slims_error(
        self, mock_get_imaging_data: MagicMock
    ):
        """Tests get_spim_data_from_slims method when subject_id empty"""
        handler = ImagingSessionHandler(
            session=MagicMock(fetch=mock_get_imaging_data)
        )
        with pytest.raises(ValueError) as e:
            handler.get_spim_data_from_slims(subject_id="")
        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
