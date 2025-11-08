from sqlalchemy.ext.asyncio import AsyncSession
from .CrudDb import CrudDB
from app.backend.main.src.core.models import Incidents


class IncidentsRepo(CrudDB[Incidents]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Incidents, session=session)
