"""Tests configs module"""

import os
import unittest
from unittest.mock import patch

from pydantic import SecretStr

from aind_slims_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(
        os.environ,
        {
            "SLIMS_USERNAME": "slims_user",
            "SLIMS_PASSWORD": "slims_password",
            "SLIMS_HOST": "slims_host",
            "SLIMS_DB": "slims_db"
        },
            clear=True
    )
    def test_get_settings(self):
        """Tests settings can be set via env vars"""
        settings = Settings()
        expected_settings = Settings(
            username="slims_user",
            password=SecretStr("slims_password"),
            host="slims_host",
            db="slims_db"
        )
        assert settings == expected_settings


if __name__ == "__main__":
    unittest.main()
