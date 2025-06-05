"""Module to handle endpoint responses"""

from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from typing import Optional, List
from slims.slims import Slims
from aind_slims_service_server.handlers.instruments import InstrumentSessionHandler
from aind_slims_service_server.models import HealthCheck
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
    "/aind_instruments/{input_id}",
)
async def get_aind_instrument(
    input_id: str = Path(..., examples=["SmartSPIM4401"]),
    partial_match: bool = Query(
        False,
        description="If true, will search for a partial match that contain the input_id string",
    ),
    session: Slims = Depends(get_session),
):
    """
    ## AIND instrument metadata
    Retrieves AIND Instrument information from SLIMS.
    """
    handler = InstrumentSessionHandler(session)
    instrument_data = handler.get_instrument_data(input_id, partial_match)
    if not instrument_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instrument not found",
        )
    return instrument_data

   
