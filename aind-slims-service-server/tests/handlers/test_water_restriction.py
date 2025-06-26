"""Tests methods in water restriction handler module"""

from datetime import datetime
from typing import List
from unittest.mock import MagicMock

import pytest

from aind_slims_service_server.handlers.water_restriction import (
    WaterRestrictionSessionHandler,
)
from aind_slims_service_server.models import SlimsWaterRestrictionData


class TestSlimsWaterRestrictionHandler:
    """Tests methods in SlimsWaterRestriction class"""

    def test_get_graph(self, mock_get_water_restriction_data: MagicMock):
        """Tests _get_graph method"""
        handler = WaterRestrictionSessionHandler(
            session=MagicMock(fetch=mock_get_water_restriction_data)
        )
        G, root_nodes = handler._get_graph()
        expected_root_nodes = ["ContentEvent.15"]
        expected_edges = [("ContentEvent.15", "Content.55")]
        assert expected_root_nodes == root_nodes
        assert set(expected_edges) == set(G.edges())

    def test_get_graph_date_criteria(
        self, mock_get_water_restriction_data: MagicMock
    ):
        """Tests _get_graph method"""
        handler = WaterRestrictionSessionHandler(
            session=MagicMock(fetch=mock_get_water_restriction_data)
        )
        G, root_nodes = handler._get_graph(
            start_date_greater_than_or_equal=datetime(2024, 12, 13, 19, 43, 32)
        )
        expected_root_nodes = ["ContentEvent.15"]
        expected_edges = [("ContentEvent.15", "Content.55")]
        assert expected_root_nodes == root_nodes
        assert set(expected_edges) == set(G.edges())

    def test_parse_graph(
        self,
        mock_get_water_restriction_data: MagicMock,
        test_water_restriction_data: List[SlimsWaterRestrictionData],
    ):
        """Tests _parse_graph method."""
        handler = WaterRestrictionSessionHandler(
            session=MagicMock(fetch=mock_get_water_restriction_data)
        )
        g, root_nodes = handler._get_graph()
        wr_data = handler._parse_graph(
            g=g, root_nodes=root_nodes, subject_id="762287"
        )
        assert test_water_restriction_data == wr_data

    def test_get_wr_data_from_slims(
        self, mock_get_water_restriction_data: MagicMock
    ):
        """Tests get_wr_data_from_slims method"""
        handler = WaterRestrictionSessionHandler(
            session=MagicMock(fetch=mock_get_water_restriction_data)
        )
        wr_data = handler.get_water_restriction_data_from_slims(
            subject_id="762287"
        )
        assert len(wr_data) == 1

    def test_get_wr_data_from_slims_error(
        self, mock_get_water_restriction_data: MagicMock
    ):
        """Tests get_wr_data_from_slims method when subject_id empty"""
        handler = WaterRestrictionSessionHandler(
            session=MagicMock(fetch=mock_get_water_restriction_data)
        )
        with pytest.raises(ValueError) as e:
            handler.get_water_restriction_data_from_slims(subject_id="")

        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
