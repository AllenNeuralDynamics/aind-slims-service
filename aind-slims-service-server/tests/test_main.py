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

    def test_get_smartspim_imaging(
        self, client: TestClient, mock_get_imaging_data: MagicMock
    ):
        """Tests smartspim imaging endpoint"""
        response = client.get("/smartspim_imaging?subject_id=744742")
        assert 200 == response.status_code

    def test_get_histology_data(
        self, client: TestClient, mock_get_histology_data: MagicMock
    ):
        """Tests histology data endpoint"""
        response = client.get("/histology?subject_id=754372")
        assert 200 == response.status_code

    def test_get_water_restriction_data(
        self, client: TestClient, mock_get_water_restriction_data: MagicMock
    ):
        """Tests water restriction data endpoint"""
        response = client.get("/water_restriction?subject_id=762287")
        assert 200 == response.status_code

    def test_get_viral_injection_data(
        self, client: TestClient, mock_get_viral_injection_data: MagicMock
    ):
        """Tests viral injection data endpoint"""
        response = client.get("/viral_injections?subject_id=614178")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
