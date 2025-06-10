"""Test routes"""

from unittest.mock import MagicMock

import pytest
from starlette.testclient import TestClient


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json()["status"] == "OK"


class TestEcephysSessionsRoute:
    """Test ecephys sessions responses."""

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


if __name__ == "__main__":
    pytest.main([__file__])
