#!/bin/bash

# Template Dockerfile path
template_dockerfile="bin/Dockerfile-template"

# Read the content of the template Dockerfile (python 3.13)
if [[ ! -f "$template_dockerfile" ]]; then
    echo "Template Dockerfile does not exist: $template_dockerfile"
    exit 1
fi

# Read the content of the Dockerfile template
dockerfile_content=$(<"$template_dockerfile")

# Python versions to generate Dockerfiles for
python_versions=("3.11" "3.12" "3.13")

# Corresponding directories for each version
directories=("dockerfiles/python311" "dockerfiles/python312" "dockerfiles/python313")

# Loop over the Python versions and directories
for i in "${!python_versions[@]}"; do
  version="${python_versions[$i]}"
  dir="${directories[$i]}"

  # Create the directory if it doesn't exist
  mkdir -p "$dir"

  # Replace only the ARG PYTHON_VERSION=3.13 line with the specific version
  updated_content="${dockerfile_content//ARG PYTHON_VERSION=bleh/ARG PYTHON_VERSION=$version}"

  # Save the new Dockerfile
  echo "$updated_content" > "$dir/Dockerfile"

  echo "Generated Dockerfile for Python $version in $dir"
done
