"""Tests configs module"""

import os
import unittest
from unittest.mock import patch
from pydantic import SecretStr
from aind_slims_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(os.environ, {"MYENV_HOST": "example"}, clear=True)
    def test_get_settings(self):
        """Tests settings can be set via env vars"""
        settings = Settings(
            host="abc.def",
            port=1234,
            username="user",
            password="pass",
            database="db",
        )
        expected_settings = Settings(
            host="abc.def",
            port=1234,
            username="user",
            password=SecretStr("pass"),
            database="db",
        )
        assert settings == expected_settings


if __name__ == "__main__":
    unittest.main()
