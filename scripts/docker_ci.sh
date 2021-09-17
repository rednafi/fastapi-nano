#!/usr/bin/env bash

# Automatically update dependencies and run the tests.
# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

current_dir=$(pwd)
cookiecutter_dir=\{\{cookiecutter.repo\}\}

# Install the dependencies.
pip install -r $cookiecutter_dir/requirements-dev.txt  &&\
pip install -r $cookiecutter_dir/requirements.txt

# Create a concrete project from the cookiecutter template.
cookiecutter $current_dir --no-input -f

# Run the tests.
cd fastapi-nano && pytest && cd ..

# Build docker-container.
docker-compose -f fastapi-nano/docker-compose.yml up --build -d

# Cleanup.
docker-compose -f fastapi-nano/docker-compose.yml down
## rm -rf fastapi-nano

# turn off command echo
set +x
