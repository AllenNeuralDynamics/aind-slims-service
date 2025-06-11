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

    def test_get_404_ecephys_sessions(
        self, client: TestClient, mock_get_ecephys_data: MagicMock
    ):
        """Tests a missing data response"""
        response = client.get("/ecephys_sessions?subject_id=0")
        expected_response = {"detail": "Not found"}
        assert response.status_code == 404
        assert response.json() == expected_response


# TODO: replace these tests and add to TestRoutes suite
class TestInstrumentRoute:
    """Test instrument responses."""

    @patch(
        "aind_slims_service_server.handlers.instrument."
        "InstrumentSessionHandler.get_instrument_data"
    )
    def test_get_200_instrument(
        self, mock_get_instrument, client, test_slims_instrument
    ):
        """Tests aind_instrument endpoint"""
        mock_get_instrument.return_value = test_slims_instrument
        response = client.get("/aind_instruments/SmartSPIM2-2")
        assert response.status_code == 200
        assert response.json() == test_slims_instrument

    @patch(
        "aind_slims_service_server.handlers.instrument."
        "InstrumentSessionHandler.get_instrument_data"
    )
    def test_get_404_instrument(self, mock_get_instrument, client):
        """Tests aind_instrument endpoint with non-existent instrument"""
        mock_get_instrument.return_value = None
        response = client.get("/aind_instruments/nonExistentInstrument")
        assert response.status_code == 404
        assert response.json() == {"detail": "Instrument not found"}

    @patch(
        "aind_slims_service_server.handlers.instrument."
        "InstrumentSessionHandler.get_instrument_data"
    )
    def test_200_get_partial_match_instrument(
        self, mock_get_instrument, client, test_slims_instrument
    ):
        """Tests aind_instrument endpoint with partial match"""
        mock_get_instrument.return_value = [test_slims_instrument]
        response = client.get("/aind_instruments/SmartSPIM?partial_match=true")
        assert response.status_code == 200
        assert response.json() == [test_slims_instrument]

    @patch(
        "aind_slims_service_server.handlers.instrument."
        "InstrumentSessionHandler.get_instrument_data"
    )
    def test_500_get_instrument_error(self, mock_get_instrument, client):
        """Tests aind_instrument endpoint with an error"""
        mock_get_instrument.side_effect = Exception("Something went wrong")
        response = client.get("/aind_instruments/SmartSPIM2-2")
        assert response.status_code == 500

if __name__ == "__main__":
    pytest.main([__file__])
