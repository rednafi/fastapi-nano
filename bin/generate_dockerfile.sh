#!/usr/bin/env bash

set -euo pipefail

# Template Dockerfile path
template_dockerfile="bin/Dockerfile-template"

# Read the content of the Dockerfile template.
if [[ ! -f "$template_dockerfile" ]]; then
    echo "Template Dockerfile does not exist: $template_dockerfile"
    exit 1
fi

dockerfile_content=$(<"$template_dockerfile")

# Python versions to generate Dockerfiles for
python_versions=("3.13" "3.14")

# Corresponding directories for each version
directories=("dockerfiles/python313" "dockerfiles/python314")

# Loop over the Python versions and directories
for i in "${!python_versions[@]}"; do
  version="${python_versions[$i]}"
  dir="${directories[$i]}"

  # Create the directory if it doesn't exist
  mkdir -p "$dir"

  updated_content="${dockerfile_content//ARG PYTHON_VERSION=bleh/ARG PYTHON_VERSION=$version}"

  # Save the new Dockerfile
  echo "$updated_content" > "$dir/Dockerfile"

  echo "Generated Dockerfile for Python $version in $dir"
done
