"""Main FastAPI application."""

from fastapi import FastAPI
from plantpy import __version__

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Root endpoint."""
    return {
        "PlantPy": "Python API for house plants.",
        "version": __version__,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000)  # noqa: S104
