"""Test routes"""

import pytest
from unittest.mock import patch


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json()["status"] == "OK"


class TestEcephysSessionsRoute:
    """Test ecephys sessions responses."""

    @patch(
        "aind_slims_service_server.handlers.ecephys."
        "EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_get_200_ecephys_sessions(
        self, mock_get_ephys, client, test_ecephys_data
    ):
        """Tests a good response"""
        mock_get_ephys.return_value = test_ecephys_data
        response = client.get("/ecephys_sessions")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["subject_id"] == "750108"

    @patch(
        "aind_slims_service_server.handlers.ecephys."
        "EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_get_404_ecephys_sessions(self, mock_get_ephys, client):
        """Tests a missing data response"""
        mock_get_ephys.return_value = []
        response = client.get("/ecephys_sessions?subject_id=0")
        expected_response = {"detail": "Not found"}
        assert response.status_code == 404
        assert response.json() == expected_response

    @patch(
        "aind_slims_service_server.handlers.ecephys."
        "EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_500_internal_server_error(self, mock_get_ephys, client):
        """Tests an internal server error response"""
        mock_get_ephys.side_effect = Exception("Something went wrong")
        response = client.get("/ecephys_sessions?subject_id=1234")
        assert response.status_code == 500


if __name__ == "__main__":
    pytest.main([__file__])
