"""Module to test main app"""

from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient


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

    def test_get_instrument(
        self, client: TestClient, mock_get_instrument_data: MagicMock
    ):
        """Tests instrument endpoint"""
        response = client.get("/aind_instruments/SmartSPIM2-2")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
