FROM python:3.12-slim

RUN pip install --upgrade pip && pip install poetry

WORKDIR /app/backend/main


COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install

COPY app/backend/main/main_alembic ./main_alembic
COPY app/backend/main/src/core/models ./src/core/models
COPY app/backend/main/src/core/configs ./src/core/configs

WORKDIR /app/backend/main/main_alembic

ENTRYPOINT ["alembic"]
CMD ["revision", "--autogenerate"]
