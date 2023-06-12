#!/usr/bin/env bash

# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

# Delete dep files.
rm -rf requirements-*.txt

# Install dev dependencies.
pip install pip-tools

# Update the deps.
pip-compile -o requirements.txt pyproject.toml --no-emit-options
pip-compile -o requirements-dev.txt pyproject.toml --extra=dev --no-emit-options
