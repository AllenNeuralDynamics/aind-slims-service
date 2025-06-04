"""Set up fixtures to be used across all test modules."""

import json
import os
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from slims.internal import Record

from aind_slims_service_server.configs import Settings
from aind_slims_service_server.main import app
from aind_slims_service_server.models import (
    EcephysRewardSpouts,
    EcephysStreamModule,
    SlimsEcephysData,
)
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
        return base if subdir is None else base / subdir

    return _get


@pytest.fixture(scope="session")
def load_json(resources_dir):
    """Fixture to load a JSON file from any resource subdirectory."""

    def _load(filename, subdir=None):
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
def test_ecephys_data():
    """Reusable expected SlimsEcephysData for ecephys handler tests."""
    return [
        SlimsEcephysData(
            experiment_run_created_on=datetime(
                2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc
            ),
            subject_id="750108",
            operator="Person Merson",
            instrument=None,
            session_type="Dynamic Foraging",
            device_calibrations=None,
            mouse_platform_name="Dynamic Foraging",
            active_mouse_platform=True,
            session_name="ecephys_750108_2024-12-23_14-51-45",
            animal_weight_prior=Decimal("30.2"),
            animal_weight_after=Decimal("30.5"),
            animal_weight_unit="g",
            reward_consumed=Decimal("1"),
            reward_consumed_unit="ml",
            stimulus_epochs=410,
            link_to_stimulus_epoch_code=("git@github.com:SomeLink.git"),
            reward_solution="Water",
            other_reward_solution=None,
            reward_spouts=[
                EcephysRewardSpouts(
                    spout_side="Water",
                    starting_position=None,
                    variable_position=None,
                )
            ],
            stream_modalities=["Behavior", "Behavior Videos", "Ecephys"],
            stream_modules=[
                EcephysStreamModule(
                    implant_hole=5,
                    assembly_name="50209",
                    probe_name="50209",
                    primary_target_structure="Retrosplenial area",
                    secondary_target_structures=None,
                    arc_angle=Decimal("-17.0"),
                    module_angle=Decimal("12.0"),
                    rotation_angle=Decimal("0.0"),
                    coordinate_transform=(
                        "calibration_info_np2_2024_12_23T11_36_00.xlsx"
                    ),
                    ccf_coordinate_ap=Decimal("0.5"),
                    ccf_coordinate_ml=Decimal("0.5"),
                    ccf_coordinate_dv=Decimal("0.5"),
                    ccf_coordinate_unit="&mu;m",
                    ccf_version=None,
                    bregma_target_ap=Decimal("0.5"),
                    bregma_target_ml=Decimal("0.5"),
                    bregma_target_dv=Decimal("0.5"),
                    bregma_target_unit="mm",
                    surface_z=Decimal("5508.5"),
                    surface_z_unit="&mu;m",
                    manipulator_x=Decimal("7610.0"),
                    manipulator_y=Decimal("9063.0"),
                    manipulator_z=Decimal("6703.0"),
                    manipulator_unit="&mu;m",
                    dye="DiI",
                )
            ],
            daq_names=["Basestation Slot 3"],
            camera_names=[
                "Bottom camera",
                "Eye camera",
                "Side camera left",
            ],
        )
    ]
