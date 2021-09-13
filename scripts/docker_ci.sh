#!/usr/bin/env bash

# Automatically update dependencies and run the tests.
# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

# Install the dependencies.
pip install -r \{\{cookiecutter.repo\}\}/requirements-dev.txt &&\
pip install -r \{\{cookiecutter.repo\}\}/requirements.txt

# Create a concrete project from the cookiecutter template.
cookiecutter $(pwd) --no-input -f

# Run the tests.
pytest fastapi-nano

# Build docker-container.
docker-compose -f fastapi-nano/docker-compose.yml up --build -d

# Cleanup.
docker-compose -f fastapi-nano/docker-compose.yml down
rm -rf fastapi-nano

# turn off command echo
set +x
