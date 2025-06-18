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

class SlimsViralMaterialData(BaseModel):
    """Model for viral material data."""

    content_category: Optional[str] = "Viral Materials"
    content_type: Optional[str] = None
    content_created_on: Optional[AwareDatetime] = None
    content_modified_on: Optional[AwareDatetime] = None
    viral_solution_type: Optional[str] = None
    virus_name: Optional[str] = None
    lot_number: Optional[str] = None
    lab_team: Optional[str] = None
    virus_type: Optional[str] = None
    virus_serotype: Optional[str] = None
    virus_plasmid_number: Optional[str] = None
    name: Optional[str] = None
    dose: Optional[Decimal] = None
    dose_unit: Optional[str] = None
    titer: Optional[Decimal] = None
    titer_unit: Optional[str] = "GC/ml"
    volume: Optional[Decimal] = None
    volume_unit: Optional[str] = None
    date_made: Optional[AwareDatetime] = None
    intake_date: Optional[AwareDatetime] = None
    storage_temperature: Optional[str] = None
    special_storage_guidelines: Optional[List[str]] = []
    special_handling_guidelines: Optional[List[str]] = []
    parent_name: Optional[str] = None
    mix_count: Optional[int] = None
    derivation_count: Optional[int] = None
    ingredient_count: Optional[int] = None


class SlimsViralInjectionData(BaseModel):
    """ "Model for viral injection data."""

    content_category: Optional[str] = "Viral Materials"
    content_type: Optional[str] = "Viral Injection"
    content_created_on: Optional[AwareDatetime] = None
    content_modified_on: Optional[AwareDatetime] = None
    name: Optional[str] = None
    viral_injection_buffer: Optional[str] = None
    volume: Optional[Decimal] = None
    volume_unit: Optional[str] = None
    labeling_protein: Optional[str] = None
    date_made: Optional[AwareDatetime] = None
    intake_date: Optional[AwareDatetime] = None
    storage_temperature: Optional[str] = None
    special_storage_guidelines: Optional[List[str]] = []
    special_handling_guidelines: Optional[List[str]] = []
    mix_count: Optional[int] = None
    derivation_count: Optional[int] = None
    ingredient_count: Optional[int] = None

    # From ORDER table
    assigned_mice: Optional[List[str]] = []
    requested_for_date: Optional[int] = None
    planned_injection_date: Optional[AwareDatetime] = None
    planned_injection_time: Optional[AwareDatetime] = None
    order_created_on: Optional[int] = None

    viral_materials: Optional[List[SlimsViralMaterialData]] = []