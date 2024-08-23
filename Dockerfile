FROM python:3.12-slim

LABEL authors="Арсений"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && POETRY_VIRTUALENVS_CREATE=false poetry install --without test --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY . .
CMD alembic upgrade head && python app/main.py
