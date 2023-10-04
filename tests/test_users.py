import pytest


@pytest.mark.parametrize(
    "username, email, password, role",
    [
        ("jhon", "jhon@gmail.com", "jhon", "admin"),
        ("ucup", "ucup@gmail.com", "ucup", "user"),
        ("asep", "asep@gmail.com", "asep", "user"),
    ],
)
def test_create_user(client, username, email, password, role):
    response = client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password, "role": role},
    )

    assert response.status_code == 201


@pytest.mark.parametrize(
    "username, email, password, role",
    [
        (None, None, None, None),
        (" ", " ", " ", " "),
        ("jhon", "jhon@gmail.com", "jhon", "hacker"),
        ("jhon", "jhon@gmail.com", "", "admin"),
        ("jhon", "", "jhon", "admin"),
        ("", "jhon@gmail.com", "jhon", "admin"),
        ("jhon", "invalid_email", "jhon", "admin"),
    ],
)
def test_invalid_create_user(client, username, email, password, role):
    response = client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password, "role": role},
    )

    assert response.status_code == 422


def test_create_user_without_body(client):
    response = client.post("/api/users/")

    assert response.status_code == 415


def test_create_user_without_json_data(client):
    response = client.post("/api/users/", json={})

    assert response.status_code == 400


def test_invalid_create_user_with_same_email(client):
    # create new user
    client.post(
        "/api/users/",
        json={"username": "jhon", "email": "jhon@gmail.com", "password": "jhon"},
    )

    response = client.post(
        "api/users/",
        json={"username": "doe", "email": "jhon@gmail.com", "password": "doe"},
    )

    # invalid, email exist in db
    assert response.status_code == 409


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_get_current_user(client, username, email, password):
    # create new user
    client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password},
    )

    # login
    login_response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    login_json = login_response.json
    access_token = login_json["data"]["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    # get user with sending token
    response = client.get("/api/users/me", headers=headers)

    assert response.status_code == 200


def test_get_current_user_without_token(client):
    response = client.get("/api/users/me")

    assert response.status_code == 401


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_get_current_user_with_fake_access_token(client, username, email, password):
    fake_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDA5MTMxOCwianRpIjoiNDE5NDg1YWYtOTk5Yi00OTEzLWE4ZDctZjdmMGU0NDRlODlmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk0MDkxMzE4LCJleHAiOjE2OTQwOTMxMTh9.Rm0zvd5IZjEiILRwKuPRCQxN8uH1i77T-HFuDj-H_KA"

    # create new user
    client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password},
    )

    # get user with sending fake token
    headers = {"Authorization": f"Bearer {fake_access_token}"}
    response = client.get("/api/users/me", headers=headers)

    assert response.status_code == 422
