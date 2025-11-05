.PHONY: setup run lint format test precommit-install build

PY?=python3
POETRY?=poetry

setup:
	$(PY) -m pip install -U pip setuptools wheel
	$(PY) -m pip install -U poetry
	$(POETRY) install --no-interaction

run:
	$(POETRY) run python -m visualizations.app.main

lint:
	$(POETRY) run ruff check .
	$(POETRY) run black --check .
	$(POETRY) run isort --check-only .
	$(POETRY) run mypy .

format:
	$(POETRY) run ruff check . --fix
	$(POETRY) run black .
	$(POETRY) run isort .

test:
	$(POETRY) run pytest

precommit-install:
	$(POETRY) run pre-commit install

build:
	docker build -t visualizations .
