"""Tests methods in models module"""

import unittest
from datetime import datetime, timezone
from aind_slims_service_server.models import (
    SlimsEcephysData,
    HealthCheck,
)


class TestHealthCheck(unittest.TestCase):
    """Tests for HealthCheck class"""

    def test_constructor(self):
        """Basic test for class constructor"""

        health_check = HealthCheck()
        self.assertEqual("OK", health_check.status)


class TestSlimsEcephysData(unittest.TestCase):
    """Tests for SlimsEcephysData class"""

    def test_constructor(self):
        """Basic test for class constructor"""

        ecephys_data = SlimsEcephysData(
            subject_id="750108",
        )
        self.assertEqual("750108", ecephys_data.subject_id)

    def test_date_str_conversion(self):
        """Test date string conversion"""

        date_str = "2025-01-01T00:00:00Z"
        expeeted_dt = datetime(2025, 1, 1, 0, 0, tzinfo=timezone.utc)

        ecephys_data = SlimsEcephysData(
            subject_id="750108",
            session_name="test_session",
            experiment_run_created_on=date_str,
        )
        ecephys_data.model_validate(ecephys_data.model_dump())
        self.assertEqual(expeeted_dt, ecephys_data.experiment_run_created_on)


if __name__ == "__main__":
    unittest.main()
