# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=1 \
    PORT=8050

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install --upgrade pip setuptools wheel && \
    pip install poetry

WORKDIR /app

# Only project metadata first (for better layering)
COPY pyproject.toml README.md /app/

# Install deps
RUN poetry install --no-ansi --no-interaction --no-root

# Copy source
COPY src /app/src
COPY configs /app/configs

EXPOSE 8050
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:${PORT}", "visualizations.app.main:server"]
