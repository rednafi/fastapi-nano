import logging

"""Test suite for the logger module."""

import logging
from collections.abc import Iterator
from io import StringIO

import pytest
from _pytest.logging import LogCaptureFixture  # for caplog fixture typing

from svc.core.logger import configure_logger


@pytest.fixture
def canned_logger() -> Iterator[logging.Logger]:
    """Fixture to configure the logger for tests with propagate set to True."""
    logger = logging.getLogger("fnano")

    # Clear any handlers attached to the logger from previous tests
    logger.handlers = []

    # Call the function that configures the logger
    configure_logger()

    # Set logger propagation to True for tests
    original_propagate = logger.propagate
    logger.propagate = True

    # Yield the logger for use in tests
    yield logger

    # Reset the logger propagate to the original value after test
    logger.propagate = original_propagate


def test_configure_logger(
    canned_logger: logging.Logger, caplog: LogCaptureFixture
) -> None:
    # Test if logger is configured properly
    with caplog.at_level(logging.INFO, logger="fnano"):
        canned_logger.info("Test log message")

    # Check if the log was captured and formatted correctly
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[0].message == "Test log message"

    # Check if the time format in the log is correct
    log_time = caplog.records[0].asctime
    assert isinstance(log_time, str)
    assert len(log_time) == 19  # "YYYY-MM-DD HH:MM:SS" is 19 characters long


def test_log_output_format(canned_logger: logging.Logger) -> None:
    # Set up a StringIO stream to capture log output
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    canned_logger.handlers = []  # Remove any pre-existing handlers
    canned_logger.addHandler(handler)
    canned_logger.setLevel(logging.INFO)

    # Log a message and capture the output
    canned_logger.info("Test log message")

    # Flush the handler and get the output
    handler.flush()
    log_output = stream.getvalue()

    # Check the log output format
    assert "fnano - INFO - Test log message" in log_output
    assert log_output.startswith("20")  # The log should start with a year like "2024"
