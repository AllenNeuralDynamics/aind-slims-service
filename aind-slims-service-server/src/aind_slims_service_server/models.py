"""Models and schema definitions for backend data structures"""

from typing import Literal, Optional, List
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field

from aind_slims_service_server import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__


def alias(model, field):
    """Get the alias for a field from a Pydantic model."""
    return model.model_fields[field].alias


class Content(BaseModel):
    """Expected Content from SLIMS"""

    pk: int = Field(..., alias="cntn_pk")
    category: Optional[str] = Field(default=None, alias="cntn_fk_category")
    type: Optional[str] = Field(default=None, alias="cntn_fk_contentType")
    viral_solution: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_viralSolutionType"
    )
    solution_name: Optional[str] = Field(
        default=None, alias="cntn_cf_solutionName"
    )
    antibody: Optional[str] = Field(default=None, alias="cntn_cf_antibody")
    amplifier_name: Optional[str] = Field(
        default=None, alias="cntn_cf_HCRamplifierName"
    )
    probe_name: Optional[str] = Field(
        default=None, alias="cntn_cf_HCRprobeName"
    )
    odorant_name: Optional[str] = Field(
        default=None, alias="cntn_cf_odorantName"
    )
    reagent: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_reagentName"
    )
    dye_name: Optional[str] = Field(default=None, alias="cntn_cf_dyeName")
    virus_name: Optional[str] = Field(default=None, alias="cntn_cf_virusName")
    collection: Optional[str] = Field(
        default=None, alias="cntn_collectionDate"
    )
    deprecated_catalog_number: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_dyeCatalogNumber"
    )
    catalog_number_hcr: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_catalogNumberHcrProbes"
    )
    catalog_number_hcr: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_catalogNumberHcrAmplifiers"
    )
    catalog_number_ex: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_catalogNumberReagents"
    )
    catalog_number: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_catalogNumberOdorants"
    )
    catalog_number: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_catalogNumberAntibodies"
    )
    catalog_number: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_catalogNumberDyes"
    )
    manufacturer: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_manufacturer"
    )
    lot_number: Optional[str] = Field(default=None, alias="cntn_cf_lotNumber")
    lab: Optional[str] = Field(default=None, alias="cntn_cf_fk_labTeam")
    container: Optional[str] = Field(
        default=None, alias="cntn_fk_containerContentType"
    )
    virus: Optional[str] = Field(default=None, alias="cntn_cf_fk_virusType")
    accession_id: Optional[str] = Field(
        default=None, alias="cntn_cf_accessionId"
    )
    hcr_probe: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_HCRProbegene"
    )
    antibody: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_antibodyType"
    )
    subcellular_localization: Optional[str] = Field(
        default=None, alias="cntn_cf_dyeSubcellularLocalization"
    )
    color: Optional[str] = Field(default=None, alias="cntn_cf_fk_dyeColor")
    antibody_target: Optional[str] = Field(
        default=None, alias="cntn_cf_antibodyTarget"
    )
    host: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_antibodyHostSpecies"
    )
    virus: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_virusSerotype"
    )
    hcr: Optional[str] = Field(default=None, alias="cntn_cf_fk_hcrAmplifier")
    virus_plasmid_number: Optional[str] = Field(
        default=None, alias="cntn_cf_virusPlasmidNumber"
    )
    conjugation: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_antibodyConjugationState"
    )
    baseline_weight: Optional[Decimal] = Field(
        default=None, alias="cntn_cf_baselineWeight"
    )
    hairpin: Optional[str] = Field(default=None, alias="cntn_cf_fk_hairpin")
    water_restricted: Optional[bool] = Field(
        default=None, alias="cntn_cf_waterRestricted"
    )
    hcr_probe: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_hcrProbeSpecies"
    )
    clone: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_antibodyCloneType"
    )
    name: Optional[str] = Field(default=None, alias="cntn_id")
    fluorophore: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_antibodyFluorophore"
    )
    excitation_wavelength: Optional[Decimal] = Field(
        default=None, alias="cntn_cf_excitationWavelength"
    )
    dose: Optional[Decimal] = Field(default=None, alias="cntn_cf_dose")
    emission_wavelength: Optional[Decimal] = Field(
        default=None, alias="cntn_cf_emissionWavelength"
    )
    titer: Optional[Decimal] = Field(default=None, alias="cntn_cf_titer")
    barcode: Optional[str] = Field(default=None, alias="cntn_barCode")
    viral_injection: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_viralInjectionBuffer"
    )
    volume: Optional[Decimal] = Field(
        default=None, alias="cntn_cf_volumeRequired"
    )
    mass: Optional[Decimal] = Field(default=None, alias="cntn_cf_massRequired")
    concentration_quant: Optional[Decimal] = Field(
        default=None, alias="cntn_cf_concentrationQuant"
    )
    concentration: Optional[str] = Field(
        default=None, alias="cntn_cf_solutionConcentration"
    )
    date_made: Optional[str] = Field(default=None, alias="cntn_cf_dateMade")
    ph: Optional[str] = Field(default=None, alias="cntn_cf_ph_shortText")
    product: Optional[str] = Field(default=None, alias="cntn_fk_product")
    dilution: Optional[str] = Field(default=None, alias="cntn_dilutionFactor")
    intake_date: Optional[str] = Field(
        default=None, alias="cntn_cf_intakeDate"
    )
    intake_date: Optional[str] = Field(
        default=None, alias="cntn_cf_intakeDate_NA"
    )
    expiry_date: Optional[str] = Field(
        default=None, alias="cntn_cf_expiryDate"
    )
    user: Optional[str] = Field(default=None, alias="cntn_fk_user")
    storage: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_storageTemp_dynChoice"
    )
    breeding_group: Optional[str] = Field(
        default=None, alias="cntn_cf_labtracksGroup"
    )
    special_storage: Optional[List[str]] = Field(
        default=[], alias="cntn_cf_fk_specialStorageGuidelines"
    )
    full_genotype: Optional[str] = Field(
        default=None, alias="cntn_cf_genotype"
    )
    sex_fixed: Optional[str] = Field(default=None, alias="cntn_cf_sex")
    date_of_birth: Optional[str] = Field(
        default=None, alias="cntn_cf_dateOfBirth"
    )
    special_handling: Optional[List[str]] = Field(
        default=[], alias="cntn_cf_fk_specialHandlingGuidelines"
    )
    purity: Optional[List[str]] = Field(
        default=[], alias="cntn_cf_fk_purityStandards"
    )
    project: Optional[str] = Field(default=None, alias="cntn_cf_fk_projectId")
    open_date: Optional[str] = Field(default=None, alias="cntn_cf_openDate")
    quantity: Optional[Decimal] = Field(default=None, alias="cntn_quantity")
    group: Optional[str] = Field(default=None, alias="cntn_fk_group")
    unit: Optional[str] = Field(default=None, alias="cntn_unit")
    collection: Optional[str] = Field(
        default=None, alias="cntn_collectionTime"
    )
    source: Optional[str] = Field(default=None, alias="cntn_fk_source")
    disease: Optional[str] = Field(default=None, alias="cntn_fk_disease")
    provider: Optional[str] = Field(default=None, alias="cntn_fk_provider")
    scientific_point_of_contact: Optional[str] = Field(
        default=None, alias="cntn_cf_scientificPointOfContact"
    )
    contact_person: Optional[str] = Field(
        default=None, alias="cntn_cf_contactPerson"
    )
    location: Optional[str] = Field(default=None, alias="cntn_fk_location")
    location_including: Optional[str] = Field(
        default=None, alias="cntn_fk_location_recursive"
    )
    status: Optional[str] = Field(default=None, alias="cntn_fk_status")
    status: Optional[str] = Field(default=None, alias="cntn_status")
    located_at: Optional[str] = Field(default=None, alias="cntn_position_row")
    located_at: Optional[str] = Field(
        default=None, alias="cntn_position_column"
    )
    iq_field: Optional[str] = Field(default=None, alias="cntn_cf_iqField")
    parent_barcode: Optional[str] = Field(
        default=None, alias="cntn_cf_parentBarcode"
    )
    ehs_barcode: Optional[str] = Field(
        default=None, alias="cntn_cf_ehsBarcode"
    )
    recipe: Optional[str] = Field(default=None, alias="cntn_cf_recipe")
    subcellular_localization: Optional[str] = Field(
        default=None, alias="cntn_cf_subcellularLocalization"
    )
    external_id: Optional[str] = Field(
        default=None, alias="cntn_cf_externalId"
    )
    fluorescent_protein_fixed: Optional[List[str]] = Field(
        default=[], alias="cntn_cf_fluorescentProtein"
    )
    parent_name: Optional[str] = Field(
        default=None, alias="cntn_cf_parentName"
    )
    sop: Optional[str] = Field(default=None, alias="cntn_cf_fk_sop")
    color: Optional[str] = Field(default=None, alias="cntn_cf_color")
    lab_team: Optional[str] = Field(
        default=None, alias="cntn_cf_fk_labTeamAcronym"
    )
    batch_id: Optional[str] = Field(default=None, alias="cntn_cf_batchId")
    product_filtering_without: Optional[str] = Field(
        default=None, alias="cntn_fk_product_strain"
    )
    created_by: Optional[str] = Field(default=None, alias="cntn_createdBy")
    created_on: Optional[str] = Field(default=None, alias="cntn_createdOn")
    modified_by: Optional[str] = Field(default=None, alias="cntn_modifiedBy")
    modified_on: Optional[str] = Field(default=None, alias="cntn_modifiedOn")
    original: Optional[str] = Field(
        default=None, alias="cntn_fk_originalContent"
    )
    external: Optional[str] = Field(default=None, alias="cntn_externalId")


class ExperimentRun(BaseModel):
    """Expected Experiment Run from SLIMS"""

    pk: int = Field(..., alias="xprn_pk")
    name: Optional[str] = Field(default=None, alias="xprn_name")
    comments: Optional[str] = Field(default=None, alias="xprn_comments")
    protocol: Optional[str] = Field(
        default=None, alias="xprn_fk_experimentTemplate"
    )
    instrument: Optional[str] = Field(default=None, alias="xprn_fk_instrument")
    experiment: Optional[str] = Field(default=None, alias="xprn_fk_experiment")
    user: Optional[str] = Field(default=None, alias="xprn_fk_user")
    group: Optional[str] = Field(default=None, alias="xprn_fk_group")
    unique: Optional[str] = Field(default=None, alias="xprn_uniqueIdentifier")
    signed: Optional[str] = Field(default=None, alias="xprn_signed")
    cancelled: Optional[str] = Field(default=None, alias="xprn_cancelled")
    completed: Optional[str] = Field(default=None, alias="xprn_completed")
    completed: Optional[str] = Field(default=None, alias="xprn_completedOn")
    created_by: Optional[str] = Field(default=None, alias="xprn_createdBy")
    created_on: Optional[str] = Field(default=None, alias="xprn_createdOn")
    modified: Optional[str] = Field(default=None, alias="xprn_modifiedBy")
    modified: Optional[str] = Field(default=None, alias="xprn_modifiedOn")
    last_event: Optional[str] = Field(default=None, alias="xprn_lastEventOn")


class ExperimentRunStep(BaseModel):
    """Expected Experiment Run Step from SLIMS"""

    pk: int = Field(..., alias="xprs_pk")
    name: Optional[str] = Field(default=None, alias="xprs_name")
    comments: Optional[str] = Field(default=None, alias="xprs_comments")
    operator_dynamic: Optional[List[str]] = Field(
        default=[], alias="xprs_cf_fk_operator"
    )
    instrument_dynamic: Optional[str] = Field(
        default=None, alias="xprs_cf_fk_instrument"
    )
    user: Optional[str] = Field(default=None, alias="xprs_fk_user")
    start: Optional[str] = Field(
        default=None, alias="xprs_observationStartDate"
    )
    active: Optional[str] = Field(default=None, alias="xprs_active")
    spim_wash_type_fixed: Optional[str] = Field(
        default=None, alias="xprs_cf_spimWashType"
    )
    reagent_dynamic: Optional[List[str]] = Field(
        default=[], alias="xprs_cf_fk_reagent"
    )
    antibody_dynamic: Optional[List[str]] = Field(
        default=[], alias="xprs_cf_fk_antibody"
    )
    mass: Optional[Decimal] = Field(default=None, alias="xprs_cf_mass")
    start_time: Optional[str] = Field(default=None, alias="xprs_cf_startTime")
    end_time: Optional[str] = Field(default=None, alias="xprs_cf_endTime")
    date_performed: Optional[str] = Field(
        default=None, alias="xprs_cf_datePerformed"
    )
    protocol_dynamic: Optional[str] = Field(
        default=None, alias="xprs_cf_fk_protocol"
    )
    notes_rich: Optional[str] = Field(default=None, alias="xprs_cf_notes")
    session_type_fixed: Optional[str] = Field(
        default=None, alias="xprs_cf_sessionType"
    )
    device_calibrations: Optional[str] = Field(
        default=None, alias="xprs_cf_deviceCalibrations"
    )
    mouse_platform_name: Optional[str] = Field(
        default=None, alias="xprs_cf_mousePlatformName"
    )
    active_mouse_platform: Optional[bool] = Field(
        default=None, alias="xprs_cf_activeMousePlatform"
    )
    unique: Optional[str] = Field(default=None, alias="xprs_uniqueIdentifier")
    status: Optional[str] = Field(default=None, alias="xprs_status")
    created_by: Optional[str] = Field(default=None, alias="xprs_createdBy")
    created_on: Optional[str] = Field(default=None, alias="xprs_createdOn")
    modified_by: Optional[str] = Field(default=None, alias="xprs_modifiedBy")
    modified_on: Optional[str] = Field(default=None, alias="xprs_modifiedOn")
    last_event: Optional[str] = Field(default=None, alias="xprs_lastEventOn")


class ExperimentRunStepContent(BaseModel):
    """Expected Experiment Run Step Content from SLIMS"""

    pk: int = Field(..., alias="xrsc_pk")
    usage: Optional[str] = Field(default=None, alias="xrsc_usage")
    used: Optional[str] = Field(default=None, alias="xrsc_usedQuantity")
    unique: Optional[str] = Field(default=None, alias="xrsc_uniqueIdentifier")
    content: Optional[str] = Field(default=None, alias="xrsc_contentRemoved")
    worklist: Optional[str] = Field(default=None, alias="xrsc_workListDate")
    created_by: Optional[str] = Field(default=None, alias="xrsc_createdBy")
    created_on: Optional[str] = Field(default=None, alias="xrsc_createdOn")
    modified: Optional[str] = Field(default=None, alias="xrsc_modifiedBy")
    modified: Optional[str] = Field(default=None, alias="xrsc_modifiedOn")


class ExperimentTemplate(BaseModel):
    """Expected Experiment Template from SLIMS"""

    pk: int = Field(..., alias="xptm_pk")
    name: Optional[str] = Field(default=None, alias="xptm_name")
    unique: Optional[str] = Field(default=None, alias="xptm_uniqueIdentifier")
    short: Optional[str] = Field(default=None, alias="xptm_shortName")
    protocol: Optional[str] = Field(
        default=None, alias="xptm_fk_experimentTemplateType"
    )
    analysis: Optional[str] = Field(default=None, alias="xptm_analysisType")
    version: Optional[str] = Field(default=None, alias="xptm_version")
    version_comments: Optional[str] = Field(
        default=None, alias="xptm_versionComments"
    )
    description: Optional[str] = Field(default=None, alias="xptm_description")
    experiment_run_unique_identifier: Optional[str] = Field(
        default=None, alias="xptm_uniqueIdentifierMask"
    )
    instrument_required: Optional[str] = Field(
        default=None, alias="xptm_instrumentRequired"
    )
    instrument_type: Optional[str] = Field(
        default=None, alias="xptm_fk_instrumentType"
    )
    execute_steps_in_correct: Optional[str] = Field(
        default=None, alias="xptm_stepsInOrder"
    )
    only_the_selected_roles_can: Optional[str] = Field(
        default=None, alias="xptm_validatorRoleRestricted"
    )
    skip_protocol_run: Optional[str] = Field(
        default=None, alias="xptm_skipRunCreationForm"
    )
    only_allow_predefined: Optional[str] = Field(
        default=None, alias="xptm_onlyPredefinedBlocks"
    )
    restrict_block: Optional[str] = Field(
        default=None, alias="xptm_experimentStepTypeRestricted"
    )
    open_blocks_by: Optional[str] = Field(
        default=None, alias="xptm_openBlocksByDefault"
    )
    active: Optional[str] = Field(default=None, alias="xptm_active")
    protocol_category_fixed: Optional[str] = Field(
        default=None, alias="xptm_cf_protocolCategory"
    )
    lab: Optional[str] = Field(default=None, alias="xptm_cf_fk_labTeam")
    publication: Optional[str] = Field(
        default=None, alias="xptm_fk_publicationStatus"
    )
    from_queue: Optional[str] = Field(default=None, alias="xptm_fk_from_queue")
    to_queue: Optional[str] = Field(default=None, alias="xptm_fk_to_queue")
    created_by: Optional[str] = Field(default=None, alias="xptm_createdBy")
    created_on: Optional[str] = Field(default=None, alias="xptm_createdOn")
    modified_by: Optional[str] = Field(default=None, alias="xptm_modifiedBy")
    modified_on: Optional[str] = Field(default=None, alias="xptm_modifiedOn")


class ReferenceDataRecord(BaseModel):
    """Expected Reference Data Record from SLIMS"""

    pk: int = Field(..., alias="rdrc_pk")
    name: Optional[str] = Field(default=None, alias="rdrc_name")
    abbreviation: Optional[str] = Field(
        default=None, alias="rdrc_cf_abbreviation"
    )
    unique: Optional[str] = Field(default=None, alias="rdrc_uniqueIdentifier")
    active: Optional[str] = Field(default=None, alias="rdrc_active")
    user: Optional[str] = Field(default=None, alias="rdrc_fk_user")
    temperature: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_temperature"
    )
    sop: Optional[str] = Field(default=None, alias="rdrc_cf_fk_sop")
    catalog_number: Optional[str] = Field(
        default=None, alias="rdrc_cf_catalogNumber"
    )
    manufacturer: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_manufacturer"
    )
    temp_range_min: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_tempRangeMin"
    )
    temp_range_max: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_tempRangeMax"
    )
    group: Optional[str] = Field(default=None, alias="rdrc_fk_group")
    color: Optional[str] = Field(default=None, alias="rdrc_cf_color")
    cas_number: Optional[str] = Field(default=None, alias="rdrc_cf_casNumber")
    allowed_content_type: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_allowedContentType"
    )
    accession_id: Optional[str] = Field(
        default=None, alias="rdrc_cf_accessionId"
    )
    z_direction: Optional[str] = Field(
        default=None, alias="rdrc_cf_zDirection"
    )
    rrid: Optional[str] = Field(default=None, alias="rdrc_cf_rrid")
    y_direction: Optional[str] = Field(
        default=None, alias="rdrc_cf_yDirection"
    )
    antibody_type: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_antibodyType_dyn"
    )
    deprecated_probe_gene: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_probeGene"
    )
    hcr_probe_gene: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_hcrProbeGene"
    )
    subcellular_localization: Optional[str] = Field(
        default=None, alias="rdrc_cf_dyeSubcellularLocalization"
    )
    antibody_target: Optional[str] = Field(
        default=None, alias="rdrc_cf_antibodyTarget"
    )
    x_direction: Optional[str] = Field(
        default=None, alias="rdrc_cf_xDirection"
    )
    host_species: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_antibodyHostSpecies"
    )
    color: Optional[str] = Field(default=None, alias="rdrc_cf_fk_dyeColor")
    amplifier: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_HCRamplifier"
    )
    conjugation_state: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_antibodyConjugationState"
    )
    product_line: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_HCRproductLine"
    )
    hairpin: Optional[str] = Field(default=None, alias="rdrc_cf_fk_HCRhairpin")
    probe_species: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_HCRprobeSpecies"
    )
    clone_type: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_antibodyCloneType"
    )
    fluorophore: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_antibodyFluorophore"
    )
    binding_sites_quantity: Optional[int] = Field(
        default=None, alias="rdrc_cf_HCRProbeBindingSites"
    )
    excitation_wavelength: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_excitationWavelength"
    )
    excitation_wavelength_req: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_excitationWavelengthReq"
    )
    emission_wavelength: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_emissionWavelength"
    )
    brain_orientation_image: Optional[str] = Field(
        default=None, alias="rdrc_cf_brainOrientationImage"
    )
    substance_form: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_substanceForm"
    )
    deprecated_form: Optional[str] = Field(
        default=None, alias="rdrc_cf_reagentForm"
    )
    volume: Optional[Decimal] = Field(default=None, alias="rdrc_cf_volume")
    mass: Optional[Decimal] = Field(default=None, alias="rdrc_cf_mass")
    concentration: Optional[str] = Field(
        default=None, alias="rdrc_cf_concentration"
    )
    shelf_life_unopened: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_shelfLifeUnopened_quant"
    )
    concentration_quant: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_concentrationQuant"
    )
    ph: Optional[str] = Field(default=None, alias="rdrc_cf_pH_str")
    instrument: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_instrument"
    )
    shelf_life_opened: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_shelfLifeOpened_quant"
    )
    instrument_json_attachment: Optional[str] = Field(
        default=None, alias="rdrc_cf_instrumentJsonAttachment"
    )
    storage_temperature: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_storageTemp_dynChoice"
    )
    mouse_id: Optional[str] = Field(default=None, alias="rdrc_cf_fk_mouseId")
    special_storage_guidelines: Optional[List[str]] = Field(
        default=[], alias="rdrc_cf_fk_specialStorageGuidelines"
    )
    special_handling_guidelines: Optional[List[str]] = Field(
        default=[], alias="rdrc_cf_fk_specialHandlingGuidelines"
    )
    purity_standards: Optional[List[str]] = Field(
        default=[], alias="rdrc_cf_fk_purityStandards"
    )
    tracked_by_ehs: Optional[bool] = Field(
        default=None, alias="rdrc_cf_trackedByEhs_Bool"
    )
    offset_x_mm: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_offsetX"
    )
    notes: Optional[str] = Field(default=None, alias="rdrc_cf_notes")
    offset_y_mm: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_offsetY"
    )
    offset_z_mm: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_offsetZ"
    )
    description: Optional[str] = Field(
        default=None, alias="rdrc_cf_description"
    )
    hyperlink: Optional[str] = Field(default=None, alias="rdrc_cf_hyperlink")
    specs_document: Optional[str] = Field(
        default=None, alias="rdrc_cf_specsDocument"
    )
    msds: Optional[str] = Field(default=None, alias="rdrc_cf_msds")
    lims_id: Optional[int] = Field(default=None, alias="rdrc_cf_limsId")
    spout_side: Optional[str] = Field(default=None, alias="rdrc_cf_spoutSide")
    reward_spouts: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_rewardSpouts"
    )
    starting_position: Optional[str] = Field(
        default=None, alias="rdrc_cf_startingPosition"
    )
    dye_type: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_antibodyFluorophoreDyeType"
    )
    batch_id: Optional[str] = Field(default=None, alias="rdrc_cf_batchId")
    variable_position: Optional[bool] = Field(
        default=None, alias="rdrc_cf_variablePosition"
    )
    atlas_id: Optional[str] = Field(default=None, alias="rdrc_cf_atlasId_ST")
    project_code: Optional[str] = Field(
        default=None, alias="rdrc_cf_projectCode"
    )
    funding_source: Optional[str] = Field(
        default=None, alias="rdrc_cf_fundingSource"
    )
    message: Optional[str] = Field(default=None, alias="rdrc_cf_message")
    scientific_binomial: Optional[str] = Field(
        default=None, alias="rdrc_cf_scientificBinomial"
    )
    patch_cord_name: Optional[str] = Field(
        default=None, alias="rdrc_cf_patchCordName"
    )
    funding_source: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_fundingSource"
    )
    safe_name: Optional[str] = Field(default=None, alias="rdrc_cf_safeName")
    reward_solution: Optional[str] = Field(
        default=None, alias="rdrc_cf_rewardSolution"
    )
    business_unit: Optional[str] = Field(
        default=None, alias="rdrc_cf_businessUnit"
    )
    acronym: Optional[str] = Field(default=None, alias="rdrc_cf_acronym")
    assembly_name: Optional[str] = Field(
        default=None, alias="rdrc_cf_assemblyName"
    )
    ephys_probe_name: Optional[str] = Field(
        default=None, alias="rdrc_cf_probeName"
    )
    primary_targeted_structure: Optional[str] = Field(
        default=None, alias="rdrc_cf_fk_primaryTargetedStructure"
    )
    secondary_targeted_structures: Optional[List[str]] = Field(
        default=[], alias="rdrc_cf_fk_secondaryTargetedStructures"
    )
    arc_angle: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_arcAngle"
    )
    module_angle: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_moduleAngle"
    )
    rotation_angle: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_rotationAngle"
    )
    coordinate_transform: Optional[str] = Field(
        default=None, alias="rdrc_cf_coordinateTransform"
    )
    patch_cord_output_power: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_patchCordOutputPower"
    )
    ccf_coordinates_ap: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_ccfCoordinatesAp"
    )
    ccf_coordinates_ml: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_ccfCoordinatesMl"
    )
    ccf_coordinates_dv: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_ccfCoordinatesDv"
    )
    ccf_version: Optional[str] = Field(
        default=None, alias="rdrc_cf_ccfVersion"
    )
    bregma_target_ap: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_bregmaAP"
    )
    bregma_target_ml: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_bregmaML"
    )
    bregma_target_dv: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_bregmaDV"
    )
    fiber_names: Optional[str] = Field(
        default=None, alias="rdrc_cf_fiberNames"
    )
    annotation: Optional[str] = Field(default=None, alias="rdrc_cf_annotation")
    implant_hole: Optional[int] = Field(
        default=None, alias="rdrc_cf_implantHole"
    )
    implant_targeting_guide: Optional[str] = Field(
        default=None, alias="rdrc_cf_implantTargetingGuide"
    )
    manipulator_x: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_manipulatorX"
    )
    manipulator_y: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_manipulatory"
    )
    manipulator_z: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_manipulatorZ"
    )
    surface_z: Optional[Decimal] = Field(
        default=None, alias="rdrc_cf_surfaceZ"
    )
    dye: Optional[str] = Field(default=None, alias="rdrc_cf_fk_dye")
    did_the_insertion_attempt_succeed: Optional[bool] = Field(
        default=None, alias="rdrc_cf_insertionattemptSucceed"
    )
    fiber_connections: Optional[List[str]] = Field(
        default=[], alias="rdrc_cf_fk_fiberConnections"
    )
    specify_reward_solution: Optional[str] = Field(
        default=None, alias="rdrc_cf_specifyRewardSolution"
    )
    reference_data: Optional[str] = Field(
        default=None, alias="rdrc_fk_referenceDataType"
    )
    created_by: Optional[str] = Field(default=None, alias="rdrc_createdBy")
    created_on: Optional[str] = Field(default=None, alias="rdrc_createdOn")
    modified_by: Optional[str] = Field(default=None, alias="rdrc_modifiedBy")
    modified_on: Optional[str] = Field(default=None, alias="rdrc_modifiedOn")


class Result(BaseModel):
    """Expected Result from SLIMS"""

    pk: int = Field(..., alias="rslt_pk")
    content: Optional[str] = Field(default=None, alias="rslt_fk_content")
    test: Optional[str] = Field(default=None, alias="rslt_fk_test")
    analyte: Optional[str] = Field(default=None, alias="rslt_fk_analyte")
    observation: Optional[str] = Field(
        default=None, alias="rslt_fk_resultObservationPoint"
    )
    operator_dynamic: Optional[str] = Field(
        default=None, alias="rslt_cf_fk_operator"
    )
    date_performed: Optional[str] = Field(
        default=None, alias="rslt_cf_datePerformed"
    )
    session_name: Optional[str] = Field(
        default=None, alias="rslt_cf_sessionName"
    )
    weight: Optional[Decimal] = Field(default=None, alias="rslt_cf_weight")
    value: Optional[str] = Field(default=None, alias="rslt_value")
    waterlog_operator: Optional[str] = Field(
        default=None, alias="rslt_cf_waterlogOperator"
    )
    manual: Optional[str] = Field(default=None, alias="rslt_manualValue")
    water_earned: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_waterEarned"
    )
    sample_refractive_index: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_sampleRefractiveIndex"
    )
    sample_immersion_medium_fixed: Optional[str] = Field(
        default=None, alias="rslt_cf_sampleImmersionMedium"
    )
    water_supplement_delivered: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_waterSupplementDelivered"
    )
    water_supplement_recommended: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_waterSupplementRecommended"
    )
    total_water: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_totalWater"
    )
    software_version: Optional[str] = Field(
        default=None, alias="rslt_cf_swVersion"
    )
    software_source: Optional[str] = Field(
        default=None, alias="rslt_cf_swSource"
    )
    chamber_refractive_index: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_chamberRefractiveIndex"
    )
    chamber_immersion_medium_fixed: Optional[str] = Field(
        default=None, alias="rslt_cf_chamberImmersionMedium"
    )
    spim_brain_orientation_dynamic: Optional[str] = Field(
        default=None, alias="rslt_cf_fk_spimBrainOrientation"
    )
    ground_wire_successful: Optional[bool] = Field(
        default=None, alias="rslt_cf_groundWireSuccessful"
    )
    injectable_material_dynamic: Optional[str] = Field(
        default=None, alias="rslt_cf_fk_injectableMaterial"
    )
    total_volume_injected: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_amountInjected"
    )
    position_of_ground_wire: Optional[str] = Field(
        default=None, alias="rslt_cf_positionOfGroundWire"
    )
    instrument_json_dynamic: Optional[str] = Field(
        default=None, alias="rslt_cf_fk_instrumentJson"
    )
    stimulus_device_names: Optional[List[str]] = Field(
        default=[], alias="rslt_cf_stimulusDeviceNames"
    )
    stream_modalities_fixed: Optional[List[str]] = Field(
        default=[], alias="rslt_cf_streamModalities"
    )
    mri_scan_id: Optional[str] = Field(default=None, alias="rslt_cf_mriScanId")
    well_type: Optional[str] = Field(default=None, alias="rslt_cf_wellType")
    stimulus_name: Optional[str] = Field(
        default=None, alias="rslt_cf_stimulusName"
    )
    mouse_session_dynamic: Optional[str] = Field(
        default=None, alias="rslt_cf_fk_mouseSession"
    )
    headframe_registration: Optional[str] = Field(
        default=None, alias="rslt_cf_headframeRegistration"
    )
    animal_weight: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_animalWeight"
    )
    protective_material_fixed: Optional[str] = Field(
        default=None, alias="rslt_cf_protectiveMaterial"
    )
    primary_scan: Optional[bool] = Field(
        default=None, alias="rslt_cf_primaryScan"
    )
    ground_wire_material_fixed: Optional[str] = Field(
        default=None, alias="rslt_cf_groundWireMaterial"
    )
    session_sequence: Optional[int] = Field(
        default=None, alias="rslt_cf_sessionSequence"
    )
    stimulus_modalities_fixed: Optional[str] = Field(
        default=None, alias="rslt_cf_stimulusModalities"
    )
    reward_consumed_during_epoch: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_rewardConsumedDuringEpoch"
    )
    modules_used_in_this_stream_dynamic: Optional[List[str]] = Field(
        default=[], alias="rslt_cf_fk_modulesinStream"
    )
    daq_names_fixed: Optional[List[str]] = Field(
        default=[], alias="rslt_cf_daqNames"
    )
    camera_names_fixed: Optional[List[str]] = Field(
        default=[], alias="rslt_cf_cameraNames"
    )
    light_emitting_diode_name: Optional[str] = Field(
        default=None, alias="rslt_cf_lightEmittingDiodeName"
    )
    isoflurane_start_time: Optional[str] = Field(
        default=None, alias="rslt_cf_isofluraneStartTime"
    )
    animal_weight_prior: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_animalWeightPrior"
    )
    light_emitting_diode_excitation_power: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_lightEmittingDiodeExcitationPower"
    )
    animal_weight_post: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_animalWeightPost"
    )
    reward_delivery_dynamic: Optional[str] = Field(
        default=None, alias="rslt_cf_fk_rewardDelivery"
    )
    reward_consumed: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_rewardConsumedvolume"
    )
    isoflurane_end_time: Optional[str] = Field(
        default=None, alias="rslt_cf_isofluraneEndTime"
    )
    stimulus_epochs: Optional[str] = Field(
        default=None, alias="rslt_cf_stimulusEpochs"
    )
    laser_name: Optional[str] = Field(default=None, alias="rslt_cf_laserName")
    link_to_stimulus_epoch_code: Optional[str] = Field(
        default=None, alias="rslt_cf_linkToStimulusEpochCode"
    )
    laser_wavelength: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_laserWavelength"
    )
    laser_excitation_power: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_laserExcitationPower"
    )
    speaker_name: Optional[str] = Field(
        default=None, alias="rslt_cf_speakerName"
    )
    speaker_volume: Optional[Decimal] = Field(
        default=None, alias="rslt_cf_speakerVolume"
    )
    notes: Optional[str] = Field(default=None, alias="rslt_comments")
    unique: Optional[str] = Field(default=None, alias="rslt_uniqueIdentifier")
    stability: Optional[str] = Field(
        default=None, alias="rslt_fk_stabilityStudy"
    )
    storage: Optional[str] = Field(
        default=None, alias="rslt_fk_stabilityStudyStorage"
    )
    timepoint: Optional[str] = Field(
        default=None, alias="rslt_fk_stabilityStudyTimepoint"
    )
    batch: Optional[str] = Field(default=None, alias="rslt_fk_batch")
    aggregation: Optional[str] = Field(
        default=None, alias="rslt_aggregationMethod"
    )
    event: Optional[str] = Field(default=None, alias="rslt_eventSummary")
    value_entered: Optional[str] = Field(
        default=None, alias="rslt_valueEnteredOn"
    )
    filler: Optional[str] = Field(default=None, alias="rslt_fk_filler")
    status: Optional[str] = Field(default=None, alias="rslt_fk_status")
    worklist: Optional[str] = Field(default=None, alias="rslt_fk_workList")
    worklist: Optional[str] = Field(default=None, alias="rslt_workListDate")
    warning: Optional[str] = Field(default=None, alias="rslt_qcWarning")
    marked: Optional[str] = Field(default=None, alias="rslt_qcMarked")
    position: Optional[str] = Field(default=None, alias="rslt_qcCardPosition")
    is_a_repeat: Optional[str] = Field(default=None, alias="rslt_isARepeat")
    is_repeated: Optional[str] = Field(default=None, alias="rslt_isRepeated")
    report: Optional[str] = Field(default=None, alias="rslt_report")
    created_by: Optional[str] = Field(default=None, alias="rslt_createdBy")
    created_on: Optional[str] = Field(default=None, alias="rslt_createdOn")
    modified_by: Optional[str] = Field(default=None, alias="rslt_modifiedBy")
    modified_on: Optional[str] = Field(default=None, alias="rslt_modifiedOn")


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

    experiment_run_created_on: Optional[datetime] = None
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
