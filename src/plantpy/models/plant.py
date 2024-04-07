"""Sqlalchemy model for plant table."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import UserDB

from .base import Base


class Plant(BaseModel):
    """Plant model."""

    model_config = ConfigDict(from_attributes=True)

    name: str
    scientific_name: str
    description: str
    user_id: int


class PlantDB(Base):
    """Plant database model."""

    __tablename__ = "plant_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    scientific_name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped[UserDB] = relationship(back_populates="plants")
