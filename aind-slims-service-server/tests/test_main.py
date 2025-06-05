"""Module to test main app"""

from unittest.mock import patch

import pytest


class TestMain:
    """Tests app endpoints"""

    def test_get_healthcheck(self, client):
        """Tests healthcheck"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    @patch(
        "aind_slims_service_server.handlers.instrument."
        "InstrumentSessionHandler.get_instrument_data"
    )
    def test_get_aind_instrument(
        self, mock_get_instrument, client, test_slims_instrument
    ):
        """Tests aind_instrument endpoint"""
        mock_get_instrument.return_value = test_slims_instrument
        response = client.get("/aind_instruments/SmartSPIM2-2")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
