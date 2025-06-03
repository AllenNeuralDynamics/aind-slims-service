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

class TestSlimsEcephysDataValidator(unittest.TestCase):
    """Tests for SlimsEcephysData experiment_run_created_on validator"""

    def test_int_ms_to_datetime(self):
        ts = 1738175075574  # ms
        obj = SlimsEcephysData(experiment_run_created_on=ts)
        expected = datetime(2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc)
        self.assertEqual(obj.experiment_run_created_on, expected)

    def test_int_s_to_datetime(self):
        ts = 1738175075  # s
        obj = SlimsEcephysData(experiment_run_created_on=ts)
        expected = datetime(2025, 1, 29, 18, 24, 35, tzinfo=timezone.utc)
        self.assertEqual(obj.experiment_run_created_on, expected)

    def test_str_ms_to_datetime(self):
        ts = "1738175075574"
        obj = SlimsEcephysData(experiment_run_created_on=ts)
        expected = datetime(2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc)
        self.assertEqual(obj.experiment_run_created_on, expected)

    def test_iso_string_to_datetime(self):
        ts = "2025-01-29T18:24:35.574000+00:00"
        obj = SlimsEcephysData(experiment_run_created_on=ts)
        expected = datetime(2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc)
        self.assertEqual(obj.experiment_run_created_on, expected)

    def test_datetime_passthrough(self):
        dt = datetime(2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc)
        obj = SlimsEcephysData(experiment_run_created_on=dt)
        self.assertEqual(obj.experiment_run_created_on, dt)

    def test_none(self):
        obj = SlimsEcephysData(experiment_run_created_on=None)
        self.assertIsNone(obj.experiment_run_created_on)

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            SlimsEcephysData(experiment_run_created_on="not-a-date")

if __name__ == "__main__":
    unittest.main()
