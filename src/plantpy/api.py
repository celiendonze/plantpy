"""API functions."""

from plantpy.models import PlantDB, UserDB
from plantpy.models.session import Session


def create_user(username: str, email: str, hashed_password: str) -> UserDB:
    """Create a user."""
    user = UserDB(
        username=username,
        email=email,
        hashed_password=hashed_password,
    )
    with Session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def create_plant(user: UserDB, name: str) -> PlantDB:
    """Create a plant."""
    plant = PlantDB(
        user_id=user.id,
        name=name,
    )
    with Session() as session:
        session.add(plant)
        session.commit()
        session.refresh(plant)
    return plant
