FROM tiangolo/uvicorn-gunicorn:python3.8-slim

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY ./ /app

EXPOSE 5000
