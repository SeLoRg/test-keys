from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, Query, HTTPException, status

from app.backend.main.src import dependencies
from app.backend.main.src.core.schemas.IncidentsSchemas import (
    IncidentCreate,
    IncidentRead,
    IncidentPartialUpdate,
    IncidentsFilters,
)
from app.backend.main.src.services.MainService import MainService

incidents_router = APIRouter(prefix="/incidents", tags=["Incidents"])

users_service_dp = Annotated[MainService, Depends(dependencies.get_main_service)]


# ---- Endpoints ----
@incidents_router.post(
    "/", response_model=IncidentRead, status_code=status.HTTP_201_CREATED
)
async def create_incident(
    data: IncidentCreate,
    service: users_service_dp,
):
    return await service.create_incident(data=data)


@incidents_router.post("/list", response_model=list[IncidentRead])
async def get_incidents_by_filter(
    service: users_service_dp,
    filters: IncidentsFilters,
    limit: int = 100,
    offset: int = 0,
):
    return await service.get_incidents_list_by_filter(
        limit=limit, offset=offset, filters=filters
    )


@incidents_router.patch("/{incident_id}", response_model=IncidentRead)
async def update_incident(
    service: users_service_dp,
    incident_id: UUID,
    data: IncidentPartialUpdate,
):
    return await service.partial_update_incident(incident_id=incident_id, data=data)
