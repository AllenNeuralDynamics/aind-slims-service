"""Test routes"""

import pytest
from unittest.mock import patch, MagicMock


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json()["status"] == "OK"

# TODO: finish these up
class TestEcephysSessionsRoute:
    """Test ecephys sessions responses."""

    @patch(
        "aind_slims_service_server.handlers.ecephys.EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_get_200_ecephys_sessions(self, mock_get_ephys, client):
        """Tests a good response"""
        # TODO: add list of expected data to conftest (defined in test_ecephys.py)
        mock_get_ephys.return_value = [
            {
                "experiment_run_created_on": "2025-01-29T18:24:35.574000+00:00",
                "subject_id": "750108",
                "operator": "Person Merson",
                "session_type": "Dynamic Foraging",
                "session_name": "ecephys_750108_2024-12-23_14-51-45",
                # ... add other required fields as needed ...
            }
        ]
        response = client.get("/ecephys_sessions")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
        assert response.json()[0]["subject_id"] == "750108"

    @patch(
        "aind_slims_service_server.handlers.ecephys.EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_get_404_ecephys_sessions(self, mock_get_ephys, client):
        """Tests a missing data response"""
        mock_get_ephys.return_value = []
        response = client.get("/ecephys_sessions?subject_id=0")
        expected_response = {"detail": "Not found"}
        assert response.status_code == 404
        assert response.json() == expected_response

    @patch(
        "aind_slims_service_server.handlers.ecephys.EcephysSessionHandler.get_ephys_data_from_slims"
    )
    def test_500_internal_server_error(self, mock_get_ephys, client):
        """Tests an internal server error response"""
        mock_get_ephys.side_effect = Exception("Something went wrong")
        response = client.get("/ecephys_sessions?subject_id=1234")
        # FastAPI returns 500 for unhandled exceptions
        assert response.status_code == 500


if __name__ == "__main__":
    pytest.main([__file__])
