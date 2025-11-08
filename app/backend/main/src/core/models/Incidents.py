from sqlalchemy.orm import Mapped, mapped_column
from .Base import Base


class Incidents(Base):
    __tablename__ = "incidents"

    description: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    source: Mapped[str] = mapped_column(nullable=False)
