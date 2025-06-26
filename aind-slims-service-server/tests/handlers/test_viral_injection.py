"""Tests methods in viral injection handler module"""

from typing import List
from unittest.mock import MagicMock

import pytest

from aind_slims_service_server.handlers.viral_injection import (
    ViralInjectionSessionHandler,
)
from aind_slims_service_server.models import SlimsViralInjectionData


class TestSlimsImagingHandler:
    """Tests methods in SlimsImagingHandler class"""

    def test_get_graph(self, mock_get_viral_injection_data: MagicMock):
        """Tests _get_graph method"""

        handler = ViralInjectionSessionHandler(
            session=MagicMock(fetch=mock_get_viral_injection_data)
        )
        G, root_nodes = handler._get_graph()
        expected_root_nodes = ["Content.994", "Content.992"]
        expected_edges = [
            ("Content.994", "ContentRelation.202"),
            ("ContentRelation.202", "Content.992"),
            ("Content.994", "Order.124"),
        ]
        assert expected_root_nodes == root_nodes
        assert set(expected_edges) == set(G.edges())

    def test_parse_graph(
        self,
        mock_get_viral_injection_data: MagicMock,
        test_viral_injection_data: List[SlimsViralInjectionData],
    ):
        """Tests _parse_graph method."""
        handler = ViralInjectionSessionHandler(
            session=MagicMock(fetch=mock_get_viral_injection_data)
        )
        g, root_nodes = handler._get_graph()
        inj_data = handler._parse_graph(
            g=g, root_nodes=root_nodes, subject_id="614178"
        )
        assert test_viral_injection_data == inj_data

    def test_get_viral_injection_data_from_slims(
        self, mock_get_viral_injection_data: MagicMock
    ):
        """Tests get_viral_injection_info_from_slims method"""
        handler = ViralInjectionSessionHandler(
            session=MagicMock(fetch=mock_get_viral_injection_data)
        )
        viral_data = handler.get_viral_injection_info_from_slims(
            subject_id="614178"
        )
        assert len(viral_data) == 1

    def test_get_viral_injection_info_from_slims_error(
        self, mock_get_viral_injection_data: MagicMock
    ):
        """Tests get_viral_injection_info_from_slims when subject_id empty"""
        handler = ViralInjectionSessionHandler(
            session=MagicMock(fetch=mock_get_viral_injection_data)
        )
        with pytest.raises(ValueError) as e:
            handler.get_viral_injection_info_from_slims(subject_id="")

        assert "subject_id must not be empty!" in str(e.value)


if __name__ == "__main__":
    pytest.main([__file__])
