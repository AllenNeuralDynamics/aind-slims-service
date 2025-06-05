"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from slims.internal import Record

from aind_slims_service_server.configs import Settings
from aind_slims_service_server.main import app
from aind_slims_service_server.session import get_session


@pytest.fixture(scope="session")
def test_slims_settings():
    """Fixture for a test Settings object."""
    settings = MagicMock(spec=Settings)
    settings.db = "test_db"
    settings.username = "user"
    password_mock = MagicMock()
    password_mock.get_secret_value.return_value = "pass"
    settings.password = password_mock
    settings.host = "http://localhost"
    return settings


@pytest.fixture(scope="session")
def resources_dir():
    """Fixture to get a subdirectory under the test resources directory."""
    base = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

    def _get(subdir=None):
        """Get the path to a subdirectory under the resources directory."""
        return base if subdir is None else base / subdir

    return _get


@pytest.fixture(scope="session")
def load_json(resources_dir):
    """Fixture to load a JSON file from any resource subdirectory."""

    def _load(filename, subdir=None):
        """Load a JSON file from the specified subdirectory."""
        with open(resources_dir(subdir) / filename, "r") as f:
            return json.load(f)

    return _load


@pytest.fixture(scope="session")
def form_record():
    """Fixture to create a Record from a JSON entity."""

    def _form(json_entity):
        """Create a Record from a JSON entity."""
        return Record(json_entity=json_entity, slims_api=None)

    return _form


@pytest.fixture(scope="session")
def client(test_slims_settings):
    """Fixture to create a TestClient with overridden session."""

    def override_get_session():
        """Override get_session to use the test settings."""
        yield from get_session(settings=test_slims_settings)

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture(scope="session")
def test_slims_instrument(load_json):
    """Fixture for expected instrument data."""
    return load_json("instrument.json", subdir="aind_instruments")
