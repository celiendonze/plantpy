FROM python:3.12.2-slim-bullseye

ARG UID=${UID:-1000}
ARG GID=${GID:-$UID}
RUN groupadd --gid $GID nonroot && useradd --uid $UID --gid $GID -m nonroot

RUN mkdir /code
RUN chown -R $UID:$GID /code
WORKDIR /code


COPY ./pyproject.toml .
COPY ./README.md .
RUN python -m pip install hatch
RUN python -m hatch dep show requirements > ./requirements.txt
RUN python -m pip install -r ./requirements.txt

COPY ./src/ ./src/
RUN python -m pip install . --no-deps

COPY ./fastapi_app/ ./fastapi_app/

USER $UID:$GID

EXPOSE 8000
VOLUME [ "/code/data" ]

CMD ["uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--port", "8000"]