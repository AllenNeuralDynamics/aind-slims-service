"""Set up fixtures to be used across all test modules."""

import json
import os
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from unittest.mock import MagicMock
from typing import Any, Generator
import pytest
from fastapi.testclient import TestClient
from slims.internal import Record
from aind_slims_service_server.main import app
from aind_slims_service_server.models import (
    EcephysRewardSpouts,
    EcephysStreamModule,
    SlimsEcephysData,
)
from pytest_mock import MockFixture

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


def mock_slims_fetch(
    mocker: MockFixture, table_to_file: dict,
    resources_dir: Path = RESOURCES_DIR
) -> MagicMock:
    """
    Patch slims session.fetch to return records from resource files.
    Parameters:
    ----------
    mocker: MockFixture
        The pytest-mock fixture to patch methods.
    table_to_file: dict
        A dictionary mapping SLIMS table names to corresponding JSON files.
    resources_dir: Path
        The directory where the resource files are located.
    Returns:
    -------
    MagicMock
        A mock object that simulates the fetch method of the Slims class.
    """

    def fetch_side_effect(table, *args, **kwargs):
        """Side effect for the mock fetch method."""
        filename = table_to_file.get(table)
        with open(resources_dir / filename) as f:
            records = json.load(f)
        return [Record(json_entity=j, slims_api=None) for j in records]

    mock_get = mocker.patch("slims.slims.Slims.fetch")
    mock_get.side_effect = fetch_side_effect
    return mock_get


@pytest.fixture()
def mock_get_ecephys_data(mocker: MockFixture) -> MagicMock:
    """Expected raw ecephys data."""

    table_to_file = {
        "Content": "content.json",
        "ExperimentRun": "experiment_run.json",
        "ExperimentRunStep": "experiment_run_step.json",
        "ExperimentRunStepContent": "experiment_run_step_content.json",
        "ExperimentTemplate": "experiment_template.json",
        "ReferenceDataRecord": "reference_data_record.json",
        "Result": "result.json",
    }
    return mock_slims_fetch(mocker, table_to_file, RESOURCES_DIR / "ecephys")


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


@pytest.fixture()
def mock_get_instrument_data(mocker: MockFixture) -> MagicMock:
    """Expected raw instrument data, including attachment."""
    table_to_file = {
        "ReferenceDataRecord": "reference_data_record.json",
    }
    fetch_mock = mock_slims_fetch(
        mocker, table_to_file, RESOURCES_DIR / "instrument"
    )
    # Mock the attachment retrieval
    instrument_json_path = RESOURCES_DIR / "instrument" / "instrument.json"
    with open(instrument_json_path) as f:
        instrument_json = json.load(f)
    mock_response = MagicMock()
    mock_response.json.return_value = instrument_json
    mocker.patch(
        "aind_slims_service_server.handlers.instrument."
        "InstrumentSessionHandler._get_attachment",
        return_value=mock_response,
    )
    return fetch_mock


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c
