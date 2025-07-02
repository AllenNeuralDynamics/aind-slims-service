"""Test routes"""

from unittest.mock import MagicMock

import pytest
from starlette.testclient import TestClient


class TestRoutes:
    """Test all API routes."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json()["status"] == "OK"

    def test_get_200_ecephys_sessions(
        self, client: TestClient, mock_get_ecephys_data: MagicMock
    ):
        """Tests a good response"""
        response = client.get("/ecephys_sessions")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["subject_id"] == "750108"

    def test_get_200_instrument(
        self, client: TestClient, mock_get_instrument_data: MagicMock
    ):
        """Tests a good response for instrument data"""
        response = client.get("/aind_instruments/SmartSPIM2-2")
        assert response.status_code == 200
        data = response.json()
        assert data[0]["instrument_id"] == "SmartSPIM2-2"

    def test_get_200_partial_match_instrument(
        self, client: TestClient, mock_get_instrument_data: MagicMock
    ):
        """Tests a partial match response for instrument data"""
        response = client.get("/aind_instruments/SmartSPIM?partial_match=true")
        assert response.status_code == 200
        data = response.json()
        assert data[0]["instrument_id"] == "SmartSPIM2-2"

    def test_get_200_smartspim_imaging(
        self, client: TestClient, mock_get_imaging_data: MagicMock
    ):
        """Tests a good response for SmartSPIM imaging data"""
        response = client.get("/smartspim_imaging?subject_id=744742")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["subject_id"] == "744742"

    def test_get_200_histology_data(
        self, client: TestClient, mock_get_histology_data: MagicMock
    ):
        """Tests a good response for histology data"""
        response = client.get("/histology?subject_id=754372")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["subject_id"] == "754372"

    def test_get_200_water_restriction_data(
        self, client: TestClient, mock_get_water_restriction_data: MagicMock
    ):
        """Tests a good response for water restriction data"""
        response = client.get("/water_restriction?subject_id=762287")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["subject_id"] == "762287"

    def test_get_200_viral_injection_data(
        self, client: TestClient, mock_get_viral_injection_data: MagicMock
    ):
        """Tests a good response for viral injection data"""
        response = client.get("/viral_injections?subject_id=614178")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["assigned_mice"] == ["614178"]


if __name__ == "__main__":
    pytest.main([__file__])
