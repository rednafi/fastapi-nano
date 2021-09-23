import httpx

with httpx.Client() as client:

    # Collect the API token.
    r = client.post(
        "http://localhost:5000/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"username": "ubuntu", "password": "debian"},
    )
    token = r.json()["access_token"]

    # Use the token value to hit the API.
    r = client.get(
        "http://localhost:5000/api_a/22",
        headers={"Accept": "application/json", "Authorization": f"Bearer {token}"},
    )
    print(r.json())
