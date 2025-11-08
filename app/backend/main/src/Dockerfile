FROM python:3.12-slim AS builder

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false

RUN poetry install --without dev

COPY ./app/backend/main ./app/backend/main


FROM python:3.12-slim

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

WORKDIR /app

CMD ["uvicorn", "app.backend.main.src.main:app", "--host", "0.0.0.0", "--port", "8000"]

