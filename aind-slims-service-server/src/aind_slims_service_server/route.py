"""Module to handle endpoint responses"""

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from slims.slims import Slims

from aind_slims_service_server.handlers.ecephys import EcephysSessionHandler
from aind_slims_service_server.handlers.instrument import (
    InstrumentSessionHandler,
)
from aind_slims_service_server.handlers.histology import (
    HistologySessionHandler,
)
from aind_slims_service_server.handlers.imaging import ImagingSessionHandler
from aind_slims_service_server.models import (
    HealthCheck,
    SlimsEcephysData,
    SlimsSpimData,
    SlimsHistologyData,
)
from aind_slims_service_server.session import get_session

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/ecephys_sessions",
    response_model=List[SlimsEcephysData],
)
async def get_ecephys_sessions(
    subject_id: Optional[str] = Query(
        None,
        alias="subject_id",
        examples=["750108"],
    ),
    session_name: Optional[str] = Query(
        None,
        alias="session_name",
        description="Name of the session",
        examples=["ecephys_750108_2024-12-23_14-51-45"],
    ),
    start_date_gte: Optional[str] = Query(
        None,
        alias="start_date_gte",
        description="Experiment run created on or after. (ISO format)",
        examples=["2025-04-10T00:00:00", "2025-04-10", "2025-04-10T00:00:00Z"],
    ),
    end_date_lte: Optional[str] = Query(
        None,
        alias="end_date_lte",
        description="Experiment run created on or before. (ISO format)",
        examples=["2025-04-11T00:00:00", "2025-04-11", "2025-04-11T00:00:00Z"],
    ),
    session: Slims = Depends(get_session),
):
    """
    ## Ecephys session metadata
    Retrieves Ecephys session information from SLIMS.
    """
    slims_ecephys_sessions = EcephysSessionHandler(
        session=session
    ).get_ephys_data_from_slims(
        subject_id=subject_id,
        session_name=session_name,
        start_date_greater_than_or_equal=start_date_gte,
        end_date_less_than_or_equal=end_date_lte,
    )
    if len(slims_ecephys_sessions) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return slims_ecephys_sessions


@router.get(
    "/aind_instruments/{input_id}",
    response_model=List[Dict[str, Any]],
)
async def get_aind_instrument(
    input_id: str = Path(
        ..., examples=["440_SmartSPIM1_20240327"], description="Instrument ID"
    ),
    partial_match: bool = Query(
        False,
        description=(
            "If true, will search for a partial match"
            " that contains the input_id string"
        ),
    ),
    session: Slims = Depends(get_session),
):
    """
    ## AIND instrument metadata
    Retrieves AIND Instrument information from SLIMS.
    """
    handler = InstrumentSessionHandler(session)
    instrument_data = handler.get_instrument_data(input_id, partial_match)
    if len(instrument_data) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return instrument_data


@router.get("/smartspim_imaging", response_model=List[SlimsSpimData])
async def get_smartspim_imaging(
    subject_id: Optional[str] = Query(
        None,
        alias="subject_id",
        description="Subject ID",
        examples=["744742"],
    ),
    start_date_gte: Optional[str] = Query(
        None,
        alias="start_date_gte",
        description="Date performed on or after. (ISO format)",
        examples=["2025-02-12T00:00:00", "2025-02-12", "2025-02-12T00:00:00Z"],
    ),
    end_date_lte: Optional[str] = Query(
        None,
        alias="end_date_lte",
        description="Date performed on or before. (ISO format)",
        examples=["2025-02-13T00:00:00", "2025-02-13", "2025-02-13T00:00:00Z"],
    ),
    session: Slims = Depends(get_session),
):
    """
    ## SmartSPIM imaging metadata
    Retrieves SmartSPIM imaging information from SLIMS.
    """
    handler = ImagingSessionHandler(session)
    spim_data = handler.get_spim_data_from_slims(
        subject_id=subject_id,
        start_date_greater_than_or_equal=start_date_gte,
        end_date_less_than_or_equal=end_date_lte,
    )
    if len(spim_data) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return spim_data


@router.get("/histology", response_model=List[SlimsHistologyData])
async def get_histology_data(
    subject_id: Optional[str] = Query(
        None,
        alias="subject_id",
        description="Subject ID",
        examples=["744742"],
    ),
    start_date_gte: Optional[str] = Query(
        None,
        alias="start_date_gte",
        description="Date performed on or after. (ISO format)",
        examples=["2025-02-06T00:00:00", "2025-02-06", "2025-02-06T00:00:00Z"],
    ),
    end_date_lte: Optional[str] = Query(
        None,
        alias="end_date_lte",
        description="Date performed on or before. (ISO format)",
        examples=["2025-02-07T00:00:00", "2025-02-07", "2025-02-07T00:00:00Z"],
    ),
    session: Slims = Depends(get_session),
):
    """
    ## Histology metadata
    Retrieves histology information from SLIMS.
    """
    handler = HistologySessionHandler(session)
    histology_data = handler.get_histology_data_from_slims(
        subject_id=subject_id,
        start_date_greater_than_or_equal=start_date_gte,
        end_date_less_than_or_equal=end_date_lte,
    )
    if len(histology_data) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return histology_data
