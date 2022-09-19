FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry install --no-dev --no-root --no-interaction --no-ansi

COPY . /app

CMD ["python", "main.py"]
