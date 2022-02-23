#!/usr/bin/env bash

# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

# Delete dep files.
rm -rf requirements-*.txt

# Install dev dependencies.
pip install pip-tools

# Update the deps.
pip-compile requirements.in -o requirements.txt --no-emit-options \
    && pip-compile requirements-dev.in -o requirements-dev.txt --no-emit-options
