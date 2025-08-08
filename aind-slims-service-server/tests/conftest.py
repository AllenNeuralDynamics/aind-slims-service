"""Set up fixtures to be used across all test modules."""

import json
import os
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any, Generator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from slims.internal import Record

from aind_slims_service_server.main import app
from aind_slims_service_server.models import (
    EcephysRewardSpouts,
    EcephysStreamModule,
    HistologyReagentData,
    HistologyWashData,
    SlimsEcephysData,
    SlimsHistologyData,
    SlimsSpimData,
    SlimsViralInjectionData,
    SlimsViralMaterialData,
    SlimsWaterRestrictionData,
)

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


def mock_slims_fetch(
    mocker: MockFixture,
    table_to_file: dict,
    resources_dir: Path = RESOURCES_DIR,
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
        # noinspection PyTypeChecker
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


@pytest.fixture()
def mock_get_imaging_data(mocker: MockFixture) -> MagicMock:
    """Expected raw imaging data."""
    table_to_file = {
        "Content": "content.json",
        "ExperimentRun": "experiment_run.json",
        "ExperimentRunStep": "experiment_run_step.json",
        "ExperimentRunStepContent": "experiment_run_step_content.json",
        "ExperimentTemplate": "experiment_template.json",
        "ReferenceDataRecord": "reference_data_record.json",
        "Result": "result.json",
        "SOP": "sop.json",
        "OrderContent": "order_content.json",
        "Order": "order.json",
        "User": "user.json",
    }
    return mock_slims_fetch(mocker, table_to_file, RESOURCES_DIR / "imaging")


@pytest.fixture(scope="session")
def test_imaging_data():
    """Reusable expected SlimsSpimData for imaging handler tests."""
    return [
        SlimsSpimData(
            experiment_run_created_on=1739383241200,
            order_project_id="Some Project - Some Subproject 1",
            order_created_by="PersonS",
            specimen_id="BRN00000018",
            subject_id="744742",
            protocol_name="Imaging cleared mouse brains on SmartSPIM",
            protocol_id=(
                "<a href="
                '"https://dx.doi.org/10.17504/protocols.io.3byl4jo1rlo5/'
                'v1" '
                'target="_blank" '
                'rel="nofollow noopener noreferrer">'
                "Imaging cleared mouse brains on SmartSPIM"
                "</a>"
            ),
            date_performed=1739383260000,
            chamber_immersion_medium="Ethyl Cinnamate",
            sample_immersion_medium="Ethyl Cinnamate",
            chamber_refractive_index=Decimal(str(1.557)),
            sample_refractive_index=Decimal(str(1.557)),
            instrument_id="440_SmartSPIM1_20240327",
            experimenter_name="Person R",
            z_direction="Superior to Inferior",
            y_direction="Anterior to Posterior",
            x_direction="Left to Right",
            imaging_channels=[
                "Laser = 488; Emission Filter = 525/45",
                "Laser = 561; Emission Filter = 593/40",
                "Laser = 639; Emission Filter = 667/30",
            ],
            stitching_channels="Laser = 639, Emission Filter = 667/30",
            ccf_registration_channels=(
                "Laser = 639, Emission Filter = 667/30"
            ),
            cell_segmentation_channels=None,
        )
    ]


@pytest.fixture()
def mock_get_histology_data(mocker: MockFixture) -> MagicMock:
    """Expected raw histology data."""
    table_to_file = {
        "Content": "content.json",
        "ExperimentRun": "experiment_run.json",
        "ExperimentRunStep": "experiment_run_step.json",
        "ExperimentRunStepContent": "experiment_run_step_content.json",
        "ExperimentTemplate": "experiment_template.json",
        "ReferenceDataRecord": "reference_data_record.json",
        "SOP": "sop.json",
        "Source": "source.json",
    }
    return mock_slims_fetch(mocker, table_to_file, RESOURCES_DIR / "histology")


@pytest.fixture(scope="session")
def test_histology_data():
    """Reusable expected histology reagent data for histology handler tests."""
    return [
        SlimsHistologyData(
            procedure_name="SmartSPIM Refractive Index Matching",
            experiment_run_created_on=datetime(
                2025, 1, 29, 18, 24, 35, 574000, tzinfo=timezone.utc
            ),
            specimen_id="BRN00000002",
            subject_id="754372",
            protocol_id='<a href="https://www.protocols.io/edit/refractive-index-matching-ethyl-cinnamate-cukpwuvn" target="_blank" rel="nofollow noopener noreferrer">Refractive Index Matching - Ethyl Cinnamate</a>',
            protocol_name="Refractive Index Matching - Ethyl Cinnamate (UNPUBLISHED)",
            washes=[
                HistologyWashData(
                    wash_name="Refractive Index Matching Wash",
                    wash_type="Refractive Index Matching",
                    start_time=datetime(
                        2025, 1, 24, 18, 40, tzinfo=timezone.utc
                    ),
                    end_time=datetime(
                        2025, 1, 27, 18, 40, tzinfo=timezone.utc
                    ),
                    modified_by="PersonM",
                    reagents=[
                        HistologyReagentData(
                            name="rgntEX00000020",
                            source=None,
                            lot_number="stbk5149",
                        )
                    ],
                    mass=None,
                ),
                HistologyWashData(
                    wash_name="Refractive Index Matching Wash 2",
                    wash_type=None,
                    start_time=None,
                    end_time=None,
                    modified_by="PersonM",
                    reagents=[],
                    mass=None,
                ),
            ],
        )
    ]


@pytest.fixture()
def mock_get_water_restriction_data(mocker: MockFixture) -> MagicMock:
    """Expected raw water restriction data."""
    table_to_file = {
        "ContentEvent": "content_event.json",
        "Content": "content.json",
    }
    return mock_slims_fetch(
        mocker, table_to_file, RESOURCES_DIR / "water_restriction"
    )


@pytest.fixture(scope="session")
def test_water_restriction_data():
    """Reusable expected data for water restriction handler tests."""
    return [
        SlimsWaterRestrictionData(
            content_event_created_on=datetime(
                2024, 12, 13, 19, 43, 34, 103000, tzinfo=timezone.utc
            ),
            subject_id="762287",
            start_date=datetime(
                2024, 12, 13, 19, 43, 32, 354000, tzinfo=timezone.utc
            ),
            end_date=None,
            assigned_by="person.name",
            target_weight_fraction=Decimal("0.85"),
            baseline_weight=Decimal("28.23"),
            weight_unit="g",
        )
    ]


@pytest.fixture()
def mock_get_viral_injection_data(mocker: MockFixture) -> MagicMock:
    """Expected raw viral injection data."""
    table_to_file = {
        "Content": "content.json",
        "ContentRelation": "content_relation.json",
        "Order": "order.json",
        "ContentType": "content_type.json",
    }
    return mock_slims_fetch(
        mocker, table_to_file, RESOURCES_DIR / "viral_injection"
    )


@pytest.fixture(scope="session")
def test_viral_injection_data():
    """Reusable expected data for viral injection handler tests."""
    return [
        SlimsViralInjectionData(
            content_category="Viral Materials",
            content_type="Viral injection",
            content_created_on=None,
            content_modified_on=None,
            name="INJ00000002",
            viral_injection_buffer="AAV Buffer",
            volume=Decimal(str(98.56)),
            volume_unit="&mu;l",
            labeling_protein="tdTomato",
            date_made=1746014400000,
            intake_date=None,
            storage_temperature="4 C",
            special_storage_guidelines=["Light sensitive storage"],
            special_handling_guidelines=["BSL - 1"],
            mix_count=None,
            derivation_count=None,
            ingredient_count=None,
            assigned_mice=["614178"],
            requested_for_date=None,
            planned_injection_date=1746705600000,
            planned_injection_time=None,
            order_created_on=1746717795853,
            viral_materials=[
                SlimsViralMaterialData(
                    content_category="Viral Materials",
                    content_type="Viral solution",
                    content_created_on=1746049926016,
                    content_modified_on=None,
                    viral_solution_type="Injection Dilution",
                    virus_name="7x-TRE-tDTomato",
                    lot_number="VT5355g",
                    lab_team="Molecular Anatomy",
                    virus_type="AAV",
                    virus_serotype="PhP.eB",
                    virus_plasmid_number="AiP300001",
                    name="VRS00000029",
                    dose=Decimal(str(180000000000)),
                    dose_unit=None,
                    titer=Decimal(str(24200000000000)),
                    titer_unit="GC/ml",
                    volume=Decimal(str(8.55)),
                    volume_unit="&mu;l",
                    date_made=1746049926079,
                    intake_date=None,
                    storage_temperature="-80 C",
                    special_storage_guidelines=["Avoid freeze - thaw cycles"],
                    special_handling_guidelines=["BSL - 1"],
                    parent_name=None,
                    mix_count=1,
                    derivation_count=0,
                    ingredient_count=0,
                )
            ],
        )
    ]


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c
