from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app.core import config
from app.main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def api_token():
    # Get token.
    res = client.post(
        "/token",
        headers={"Accept": "application/x-www-form-urlencoded"},
        data={
            "username": config.API_USERNAME,
            "password": config.API_PASSWORD,
        },
    )
    res_json = res.json()

    access_token = res_json["access_token"]
    token_type = res_json["token_type"]

    return f"{token_type} {access_token}"


def test_api_a_unauthorized():
    """Should return 401."""

    # Unauthorized request.
    response = client.get("/api_a/100")
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_api_a_invalid_input(api_token):
    """Should return 422."""

    # Authorized but should raise 400 error.
    response = client.get(
        "/api_a/a",
        headers={
            "Accept": "application/json",
            "Authorization": api_token,
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_api_a_ok(api_token):
    # Successful request.
    response = client.get(
        "/api_a/200",
        headers={
            "Accept": "application/json",
            "Authorization": api_token,
        },
    )
    assert response.status_code == HTTPStatus.OK

    for val in response.json().values():
        assert isinstance(val, int)


def test_api_b_unauthorized():
    """Should return 401."""

    # Unauthorized request.
    response = client.get("/api_b/200")
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_api_b_invalid_input(api_token):
    """Should return 422."""

    # Authorized but should raise 400 error.
    response = client.get(
        "/api_b/b",
        headers={
            "Accept": "application/json",
            "Authorization": api_token,
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_api_b_ok(api_token):
    # Successful request.
    response = client.get(
        "/api_b/300",
        headers={
            "Accept": "application/json",
            "Authorization": api_token,
        },
    )
    assert response.status_code == HTTPStatus.OK

    for val in response.json().values():
        assert isinstance(val, int)
