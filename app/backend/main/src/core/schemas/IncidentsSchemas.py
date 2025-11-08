from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from app.backend.main.src.core.Enums import IncidentStatus, IncidentSource


class IncidentBase(BaseModel):
    description: str = Field(..., description="Описание инцидента")
    status: IncidentStatus = Field(
        default=IncidentStatus.NEW, description="Статус инцидента"
    )
    source: IncidentSource = Field(..., description="Источник инцидента")


class IncidentCreate(IncidentBase):
    """Схема для создания нового инцидента"""

    pass


class IncidentPartialUpdate(BaseModel):
    """Схема для частичного обновления инцидента"""

    description: Optional[str] = Field(None, description="Новое описание (опционально)")
    status: Optional[IncidentStatus] = Field(
        None, description="Новый статус (опционально)"
    )
    source: Optional[IncidentSource] = Field(
        None, description="Новый источник (опционально)"
    )


class IncidentsFilters(BaseModel):
    status: Optional[IncidentStatus] = Field(
        None, description="Новый статус (опционально)"
    )
    source: Optional[IncidentSource] = Field(
        None, description="Новый источник (опционально)"
    )


class IncidentRead(IncidentBase):
    """Схема для ответа API"""

    id: UUID
    created_at: datetime
    updated_at: datetime

    ConfigDict(from_attributes=True)
