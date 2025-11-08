from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.main.src.core.db import db
from app.backend.main.src.core.repos import IncidentsRepo
from app.backend.main.src.services.MainService import MainService


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in db.get_session():
        yield session


def get_incidents_repo(session=Depends(get_session)):
    return IncidentsRepo(session)


async def get_main_service(
    session=Depends(get_session), incident_repo=Depends(get_incidents_repo)
) -> MainService:
    return MainService(incidents_repo=incident_repo, session=session)
