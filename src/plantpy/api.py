from plantpy.models.session import Session
from plantpy.models import User, Plant


def create_user(username: str, email: str, hashed_password: str) -> User:
    """Create a user."""
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
    )
    with Session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def create_plant(user: User, name: str) -> Plant:
    """Create a plant."""
    plant = Plant(
        user_id=user.id,
        name=name,
    )
    with Session() as session:
        session.add(plant)
        session.commit()
        session.refresh(plant)
    return plant
