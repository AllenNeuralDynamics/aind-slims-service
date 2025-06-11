"""Module to test main app"""

from unittest.mock import MagicMock
from fastapi.testclient import TestClient
import pytest


class TestMain:
    """Tests app endpoints"""

    def test_get_healthcheck(self, client: TestClient):
        """Tests healthcheck"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    def test_get_ecephys_sessions(
        self, client: TestClient, mock_get_ecephys_data: MagicMock
    ):
        """Tests ecephys sessions endpoint"""
        response = client.get("/ecephys_sessions?subject_id=750108")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
