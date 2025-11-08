import logging
from uuid import UUID

from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.main.src.core.configs import settings
from app.backend.main.src.core.logging.LogMeta import LogMeta
from app.backend.main.src.core.repos import IncidentsRepo, BaseRepo

from app.backend.main.src.core.Enums import IncidentStatus, IncidentSource
from app.backend.main.src.core.schemas.IncidentsSchemas import (
    IncidentCreate,
    IncidentRead,
    IncidentPartialUpdate,
    IncidentsFilters,
)


class MainService(metaclass=LogMeta):
    logger: logging.Logger | None = None

    def __init__(
        self,
        incidents_repo: IncidentsRepo,
        session: AsyncSession,
    ):
        self.session = session
        self.incidents_repo = incidents_repo

    async def create_incident(self, data: IncidentCreate) -> IncidentRead:
        try:
            incident_data = data.model_dump()
            incident_data["status"] = data.status.value
            incident_data["source"] = data.source.value

            incident = await self.incidents_repo.create(**incident_data)

            await self.session.commit()

            return IncidentRead.model_validate(incident, from_attributes=True)

        except Exception:
            await self.session.rollback()
            raise

    async def get_incidents_list_by_filter(
        self,
        filters: IncidentsFilters,
        limit: int = 100,
        offset: int = 0,
    ) -> list[IncidentRead]:
        try:
            incident_filters = filters.model_dump(exclude_none=True)

            if incident_filters["status"] is None:
                incident_filters["status"] = filters.status.value

            if incident_filters["status"] is None:
                incident_filters["source"] = filters.source.value

            incidents = await self.incidents_repo.get_by_filter(
                limit=limit, skip=offset, **incident_filters
            )

            if len(incidents) == 0:
                return list()

            return [
                IncidentRead.model_validate(i, from_attributes=True) for i in incidents
            ]

        except Exception:
            raise

    async def partial_update_incident(
        self, incident_id: UUID, data: IncidentPartialUpdate
    ) -> IncidentRead:
        try:
            incident_data = data.model_dump(exclude_none=True)

            if incident_data["status"] is None:
                incident_data["status"] = data.status.value

            if incident_data["status"] is None:
                incident_data["source"] = data.source.value

            updated_incident = await self.incidents_repo.update_by_id(
                object_id=incident_id, **incident_data
            )

            if updated_incident is None:
                raise HTTPException(
                    status_code=404, detail={"message": "Not founded incident"}
                )

            await self.session.commit()

            return IncidentRead.model_validate(updated_incident, from_attributes=True)

        except Exception:
            await self.session.rollback()
            raise
