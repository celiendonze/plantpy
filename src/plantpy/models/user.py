"""Sqlalchemy model for user table."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .plant import PlantDB

from .base import Base


class User(BaseModel):
    """User model."""

    model_config = ConfigDict(from_attributes=True)

    username: str
    email: str
    hashed_password: str


class UserDB(Base):
    """User database model."""

    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    plants: Mapped[list[PlantDB]] = relationship(back_populates="user")
