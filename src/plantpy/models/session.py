"""Session object for database operations."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base

engine = create_engine("sqlite:///./data/plantpy.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

__all__ = ["Session"]
