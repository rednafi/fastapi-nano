# Define Python version as an argument
ARG PYTHON_VERSION=3.11

# Install uv and dependencies
FROM python:${PYTHON_VERSION}-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Show the currently running commands
SHELL ["sh", "-exc"]

# Set working directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project --locked --no-dev

# Copy the project source code into the builder stage
COPY . /app

# Final stage with minimal footprint
FROM python:${PYTHON_VERSION}-slim

# Set the working directory in the final image
WORKDIR /app

# See <https://hynek.me/articles/docker-signals/>.
STOPSIGNAL SIGINT

# Copy the virtual environment and the source code from the builder stage
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app

# Set environment variables and add venv to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the application port
EXPOSE 5001

# Entry point for running the application
ENTRYPOINT ["gunicorn", "svc.main:app", "--workers", "2", "--worker-class", \
        "uvicorn.workers.UvicornWorker",  "-b", "0.0.0.0:5001" ]
