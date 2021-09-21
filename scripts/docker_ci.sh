#!/usr/bin/env bash

# Automatically update dependencies and run the tests.
# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

# Run the tests.
pytest

# Build docker-container.
docker-compose --build -d

# Cleanup.
docker-compose down
## rm -rf fastapi-nano

# turn off command echo
set +x
