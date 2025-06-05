"""Test routes"""

from unittest.mock import patch

import pytest


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json()["status"] == "OK"


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
