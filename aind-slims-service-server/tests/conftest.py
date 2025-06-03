"""Set up fixtures to be used across all test modules."""

import os
from pathlib import Path
import json
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from requests import Response
from requests_toolbelt.sessions import BaseUrlSession
from aind_slims_service_server.models import (
    Content,
    ExperimentRun,
    ExperimentRunStep,
    ExperimentRunStepContent,
    ExperimentTemplate,
    ReferenceDataRecord,
    Result
)
from aind_slims_service_server.main import app

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

@pytest.fixture
def test_slims_settings():
    """Mock the settings instance used in the session module."""
    with patch("aind_slims_service_server.session.settings") as mock_settings:
        mock_settings.db = "test_db"
        mock_settings.username = "user"
        mock_settings.password.get_secret_value.return_value = "pass"
        mock_settings.host = "http://localhost"
        yield mock_settings

@pytest.fixture(scope="session")
def ecephys_resources_dir():
    return Path(os.path.dirname(os.path.realpath(__file__))) / "resources" / "ecephys"

@pytest.fixture(scope="session")
def load_ecephys_json(ecephys_resources_dir):
    def _load(filename):
        with open(ecephys_resources_dir / filename, "r") as f:
            return json.load(f)
    return _load

@pytest.fixture(scope="session")
def form_record():
    from slims.internal import Record
    def _form(json_entity):
        return Record(json_entity=json_entity, slims_api=None)
    return _form


@pytest.fixture(scope="session")
def client():
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c
