"""Routes for user management."""

from fastapi import APIRouter
from plantpy import api
from plantpy.models import User

user_router = APIRouter()


@user_router.post("/user")
async def new_user(username: str, email: str, hashed_password: str) -> User:
    """Create a user."""
    return api.create_user(username, email, hashed_password)
