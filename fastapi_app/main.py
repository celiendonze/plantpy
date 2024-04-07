"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from plantpy import __version__

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def read_root() -> dict:
    """Root endpoint."""
    return {
        "PlantPy": "Python API for house plants.",
        "version": __version__,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000)
