"""Module to handle endpoint responses"""

from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from typing import Optional, List
from slims.slims import Slims

from aind_slims_service_server.handlers.ecephys import EcephysSessionHandler
from aind_slims_service_server.models import SlimsEcephysData, HealthCheck
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
    ),
    start_date_gte: Optional[str] = Query(
        None,
        alias="start_date_gte",
        description="Experiment run created on or after. (ISO format)",
    ),
    end_date_lte: Optional[str] = Query(
        None,
        alias="end_date_lte",
        description="Experiment run created on or before. (ISO format)",
    ),
    session: Slims = Depends(get_session),
):
    """
    ## Ecephys session metadata
    Retrieves Ecephys session information from SLIMS.
    """
    slims_ecephys_sessions = EcephysSessionHandler(session=session).get_ephys_data_from_slims(
        subject_id=subject_id,
        session_name=session_name,
        start_date_greater_than_or_equal=start_date_gte,
        end_date_less_than_or_equal=end_date_lte,
    )
    if len(slims_ecephys_sessions) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return slims_ecephys_sessions
