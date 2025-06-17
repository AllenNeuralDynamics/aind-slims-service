"""Models and schema definitions for backend data structures"""

from decimal import Decimal
from typing import List, Literal, Optional

from pydantic import AwareDatetime, BaseModel

from aind_slims_service_server import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__


class EcephysStreamModule(BaseModel):
    """Expected Stream module information from SLIMS"""

    implant_hole: Optional[int] = None
    assembly_name: Optional[str] = None
    probe_name: Optional[str] = None
    primary_target_structure: Optional[str] = None
    secondary_target_structures: Optional[list] = None
    arc_angle: Optional[Decimal] = None
    module_angle: Optional[Decimal] = None
    rotation_angle: Optional[Decimal] = None
    coordinate_transform: Optional[str] = None
    ccf_coordinate_ap: Optional[Decimal] = None
    ccf_coordinate_ml: Optional[Decimal] = None
    ccf_coordinate_dv: Optional[Decimal] = None
    ccf_coordinate_unit: Optional[str] = None
    ccf_version: Optional[str] = None
    bregma_target_ap: Optional[Decimal] = None
    bregma_target_ml: Optional[Decimal] = None
    bregma_target_dv: Optional[Decimal] = None
    bregma_target_unit: Optional[str] = None
    surface_z: Optional[Decimal] = None
    surface_z_unit: Optional[str] = None
    manipulator_x: Optional[Decimal] = None
    manipulator_y: Optional[Decimal] = None
    manipulator_z: Optional[Decimal] = None
    manipulator_unit: Optional[str] = None
    dye: Optional[str] = None


class EcephysRewardSpouts(BaseModel):
    """Expected Reward Spouts information from SLIMS"""

    spout_side: Optional[str] = None
    starting_position: Optional[str] = None
    variable_position: Optional[bool] = None


# TODO: attachments for device_calibrations, stimulus_epochs
class SlimsEcephysData(BaseModel):
    """Expected Model that needs to be extracted from SLIMS"""

    experiment_run_created_on: Optional[AwareDatetime] = None
    subject_id: Optional[str] = None
    operator: Optional[str] = None
    instrument: Optional[str] = None
    session_type: Optional[str] = None
    device_calibrations: Optional[int] = None
    mouse_platform_name: Optional[str] = None
    active_mouse_platform: Optional[bool] = None
    session_name: Optional[str] = None
    animal_weight_prior: Optional[Decimal] = None
    animal_weight_after: Optional[Decimal] = None
    animal_weight_unit: Optional[str] = None
    reward_consumed: Optional[Decimal] = None
    reward_consumed_unit: Optional[str] = None
    stimulus_epochs: Optional[int] = None
    link_to_stimulus_epoch_code: Optional[str] = None
    reward_solution: Optional[str] = None
    other_reward_solution: Optional[str] = None
    reward_spouts: Optional[List[EcephysRewardSpouts]] = []
    stream_modalities: Optional[List[str]] = None
    stream_modules: Optional[List[EcephysStreamModule]] = []
    daq_names: Optional[List[str]] = None
    camera_names: Optional[List[str]] = None


class SlimsSpimData(BaseModel):
    """Expected Model that needs to be extracted from SLIMS"""

    experiment_run_created_on: Optional[AwareDatetime] = None
    specimen_id: Optional[str] = None
    subject_id: Optional[str] = None
    protocol_name: Optional[str] = None
    protocol_id: Optional[str] = None
    date_performed: Optional[int] = None
    chamber_immersion_medium: Optional[str] = None
    sample_immersion_medium: Optional[str] = None
    chamber_refractive_index: Optional[Decimal] = None
    sample_refractive_index: Optional[Decimal] = None
    instrument_id: Optional[str] = None
    experimenter_name: Optional[str] = None
    z_direction: Optional[str] = None
    y_direction: Optional[str] = None
    x_direction: Optional[str] = None
    imaging_channels: Optional[List[str]] = None
    stitching_channels: Optional[str] = None
    ccf_registration_channels: Optional[str] = None
    cell_segmentation_channels: Optional[List[str]] = None


class HistologyReagentData(BaseModel):
    """Expected reagent information from SLIMS."""

    name: Optional[str] = None
    source: Optional[str] = None
    lot_number: Optional[str] = None


class HistologyWashData(BaseModel):
    """Expected wash information from SLIMS."""

    wash_name: Optional[str] = None
    wash_type: Optional[str] = None
    start_time: Optional[AwareDatetime] = None
    end_time: Optional[AwareDatetime] = None
    modified_by: Optional[str] = None
    reagents: List[HistologyReagentData] = []
    mass: Optional[Decimal] = None


class SlimsHistologyData(BaseModel):
    """Expected Model that needs to be extracted from SLIMS."""

    procedure_name: Optional[str] = None
    experiment_run_created_on: Optional[AwareDatetime] = None
    specimen_id: Optional[str] = None
    subject_id: Optional[str] = None
    protocol_id: Optional[str] = None
    protocol_name: Optional[str] = None
    washes: List[HistologyWashData] = []
