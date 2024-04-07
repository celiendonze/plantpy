"""Tests for the database module."""

from plantpy.models import UserDB
from plantpy.models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def test_create_user() -> None:
    """Test creating a user."""
    with Session() as session:
        user = UserDB(
            username="test",
            email="test.test@test.com",
            hashed_password="test",
        )
        session.add(user)
        session.commit()

    with Session() as session:
        user = session.query(UserDB).filter_by(username="test").first()
        assert user.username == "test"
        assert user.email == "test.test@test.com"
        assert user.hashed_password == "test"
