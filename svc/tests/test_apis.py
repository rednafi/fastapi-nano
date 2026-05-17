from collections.abc import Iterator
from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from svc.core.config import get_settings
from svc.main import create_app


@pytest.fixture(scope="module")
def client() -> Iterator[TestClient]:
    with TestClient(create_app()) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def api_token(client: TestClient) -> str:
    # Get token.
    settings = get_settings()
    res = client.post(
        "/token",
        headers={"Accept": "application/x-www-form-urlencoded"},
        data={
            "username": settings.api_username,
            "password": settings.api_password,
        },
    )
    res_json = res.json()

    access_token = res_json["access_token"]
    token_type = res_json["token_type"]

    return f"{token_type} {access_token}"


def test_token_ok(client: TestClient) -> None:
    settings = get_settings()

    response = client.post(
        "/token",
        data={
            "username": settings.api_username,
            "password": settings.api_password,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


def test_token_invalid_password(client: TestClient) -> None:
    settings = get_settings()

    response = client.post(
        "/token",
        data={
            "username": settings.api_username,
            "password": "not-the-password",
        },
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_api_a_unauthorized(client: TestClient) -> None:
    """Should return 401."""

    # Unauthorized request.
    response = client.get("/api_a/100")
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_api_a_invalid_token(client: TestClient) -> None:
    response = client.get(
        "/api_a/100",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_api_a_invalid_input(client: TestClient, api_token: str) -> None:
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


def test_api_a_ok(client: TestClient, api_token: str) -> None:
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


def test_api_b_unauthorized(client: TestClient) -> None:
    """Should return 401."""

    # Unauthorized request.
    response = client.get("/api_b/200")
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_api_b_invalid_input(client: TestClient, api_token: str) -> None:
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


def test_api_b_ok(client: TestClient, api_token: str) -> None:
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
