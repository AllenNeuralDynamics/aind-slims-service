"""Tests methods in histology handler module"""

from typing import List
from unittest.mock import MagicMock

import pytest

from aind_slims_service_server.handlers.histology import (
    HistologySessionHandler,
)
from aind_slims_service_server.models import SlimsHistologyData


class TestHistologySessionHandler:
    """Tests methods in HistologySessionHandler class"""

    def test_get_graph(self, mock_get_histology_data: MagicMock):
        """Tests _get_graph method"""

        handler = HistologySessionHandler(
            session=MagicMock(fetch=mock_get_histology_data)
        )
        G, root_nodes = handler._get_graph()
        expected_root_nodes = ["ExperimentRun.40007"]
        expected_edges = [
            ("ExperimentRun.40007", "ExperimentRunStep.60027"),
            ("ExperimentRun.40007", "ExperimentRunStep.60028"),
            ("ExperimentRun.40007", "ExperimentRunStep.60029"),
            ("ExperimentRun.40007", "ExperimentRunStep.60030"),
            ("ExperimentRun.40007", "ExperimentRunStep.60031"),
            ("ExperimentRunStep.60027", "ExperimentRunStepContent.9"),
            ("ExperimentRunStep.60028", "SOP.24"),
            ("ExperimentRunStep.60029", "Content.138"),
            ("ExperimentRunStepContent.9", "Content.166"),
            ("Content.138", "ReferenceDataRecord.1664"),
        ]
        assert expected_root_nodes == root_nodes
        assert set(expected_edges) == set(G.edges())

    def test_parse_graph(
        self,
        mock_get_histology_data: MagicMock,
        test_histology_data: List[SlimsHistologyData],
    ):
        """Tests _parse_graph_method"""
        handler = HistologySessionHandler(
            session=MagicMock(fetch=mock_get_histology_data)
        )
        G, root_nodes = handler._get_graph()

        hist_data = handler._parse_graph(
            g=G, root_nodes=root_nodes, subject_id="754372"
        )
        assert test_histology_data == hist_data

    def test_get_hist_data_from_slims(
        self, mock_get_histology_data: MagicMock
    ):
        """Tests get_hist_data_from_slims method"""
        handler = HistologySessionHandler(
            session=MagicMock(fetch=mock_get_histology_data)
        )
        hist_data = handler.get_histology_data_from_slims(subject_id="754372")
        assert len(hist_data) == 1

    def test_get_hist_data_from_slims_error(
        self, mock_get_histology_data: MagicMock
    ):
        """Tests get_hist_data_from_slims method"""
        handler = HistologySessionHandler(
            session=MagicMock(fetch=mock_get_histology_data)
        )
        with pytest.raises(ValueError) as e:
            handler.get_histology_data_from_slims(subject_id="")
        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
