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
        "aind_slims_service_server.handlers.ecephys."
        "EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_get_ecephys_sessions(
        self, mock_get_ephys, client, test_ecephys_data
    ):
        """Tests ecephys sessions endpoint"""
        mock_get_ephys.return_value = test_ecephys_data
        response = client.get("/ecephys_sessions?subject_id=750108")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
