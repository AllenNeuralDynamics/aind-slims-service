"""Test routes"""

from unittest.mock import MagicMock, patch

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

    def test_get_404_ecephys_sessions(
        self, client: TestClient, mock_get_ecephys_data: MagicMock
    ):
        """Tests a missing data response"""
        response = client.get("/ecephys_sessions?subject_id=0")
        expected_response = {"detail": "Not found"}
        assert response.status_code == 404
        assert response.json() == expected_response

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

    def test_get_404_instrument(self, client: TestClient):
        """Tests a missing instrument response"""
        with patch("slims.slims.Slims.fetch", return_value=[]):
            response = client.get("/aind_instruments/nonExistentInstrument")
            expected_response = {"detail": "Not found"}
            assert response.status_code == 404
            assert response.json() == expected_response

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

    def test_get_404_smartspim_imaging(
        self, client: TestClient, mock_get_imaging_data: MagicMock
    ):
        """Tests a missing SmartSPIM imaging data response"""
        response = client.get("/smartspim_imaging?subject_id=0")
        expected_response = {"detail": "Not found"}
        assert response.status_code == 404
        assert response.json() == expected_response


if __name__ == "__main__":
    pytest.main([__file__])
