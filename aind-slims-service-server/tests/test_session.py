"""Tests session module"""

import pytest
from unittest.mock import patch, MagicMock
from aind_slims_service_server.session import get_session

class TestSession:
    """Test methods in Session Class"""

    @patch("aind_slims_service_server.configs.Settings")
    @patch("aind_slims_service_server.session.Slims")
    def test_get_session(mock_slims, mock_settings):
        # Set up the mock settings instance
        mock_settings.db = "test_db"
        mock_settings.username = "user"
        mock_settings.password.get_secret_value.return_value = "pass"
        mock_settings.host = "http://localhost"

        mock_session = MagicMock()
        mock_slims.return_value = mock_session

        from aind_slims_service_server.session import get_session

        session_gen = get_session()
        session = next(session_gen)

        mock_slims.assert_called_once_with(
            name="test_db",
            username="user",
            password="pass",
            url="http://localhost",
        )
        assert session == mock_session

if __name__ == "__main__":
    pytest.main([__file__])
