"""Tests session module"""

from unittest.mock import MagicMock, patch

import pytest

from aind_slims_service_server.session import get_session


class TestSession:
    """Test methods in Session Class"""

    @patch("aind_slims_service_server.session.Settings")
    @patch("aind_slims_service_server.session.Slims")
    def test_get_session(self, mock_slims, mock_settings):
        """Tests get_session method."""
        mock_settings_instance = MagicMock()
        mock_settings_instance.db = "test_db"
        mock_settings_instance.username = "user"
        password_mock = MagicMock()
        password_mock.get_secret_value.return_value = "pass"
        mock_settings_instance.password = password_mock
        mock_settings_instance.host = "http://localhost"
        mock_settings.return_value = mock_settings_instance

        mock_session = MagicMock()
        mock_slims.return_value = mock_session

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
