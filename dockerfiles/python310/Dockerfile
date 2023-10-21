
FROM python:3.10-slim-bookworm

# Set environment variables.
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory.
WORKDIR /code

# Copy dependencies.
COPY requirements.txt /code/

# Install dependencies.
RUN pip install -r requirements.txt

# Copy project.
COPY . /code/

EXPOSE 5001

ENTRYPOINT [ "gunicorn", "app.main:app", "--workers", "2", "--worker-class", \
        "uvicorn.workers.UvicornWorker",  "-b", "0.0.0.0:5001" ]
