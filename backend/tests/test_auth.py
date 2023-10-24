import pytest


@pytest.mark.parametrize(
    "username, email, password",
    [("jhon", "jhon@gmail.com", "jhon"), ("doe", "doe@gmail.com", "doe")],
)
def test_login(client, username, email, password):
    # create new user
    client.post(
        "/api/users/", json={"username": username, "email": email, "password": password}
    )

    response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    assert response.status_code == 200


def test_login_without_body(client):
    response = client.post("/api/auth/login")

    assert response.status_code == 415


def test_login_without_json_data(client):
    response = client.post("/api/auth/login", json={})

    assert response.status_code == 400


@pytest.mark.parametrize(
    "email, password",
    [
        (None, None),
        (" ", " "),
        ("invalid_email", ""),
    ],
)
def test_login_with_invalid_fields(client, email, password):
    # create new user
    client.post(
        "/api/users/",
        json={"username": "jhon", "email": "jhon@gmail.com", "password": "jhon"},
    )

    response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    assert response.status_code == 422


@pytest.mark.parametrize(
    "email, password",
    [("doe@gmail.com", "doe"), ("jhon@gmail.com", "test"), ("doe@gmail.com", "jhon")],
)
def test_login_with_wrong_data(client, email, password):
    # create new user
    client.post(
        "/api/users/",
        json={"username": "jhon", "email": "jhon@gmail.com", "password": "jhon"},
    )

    response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    assert response.status_code == 401


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_refreshing_access_token(client, username, email, password):
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
    refresh_token = login_json["data"]["refresh_token"]
    access_token = login_json["data"]["access_token"]

    # get new access token
    headers = {"Authorization": f"Bearer {refresh_token}"}
    response = client.post("/api/auth/refresh", headers=headers)
    json_data = response.json
    new_access_token = json_data["data"]["access_token"]

    assert response.status_code == 200
    assert new_access_token != access_token


def test_refreshing_access_token_without_headers(client):
    response = client.post("/api/auth/refresh")

    assert response.status_code == 401


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_refreshing_access_token_with_fake_token(client, username, email, password):
    fake_refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDA5MTMxOCwianRpIjoiMDAxNDk0ZjAtNTZjMC00Y2ZlLThkNDMtZTFhOGFmNDI1N2ZmIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTY5NDA5MTMxOCwiZXhwIjoxNjk0Njk2MTE4fQ.zpTdf4CoGx8zEfV4ajrK3q-wwaHBrb9Q_phw9ddkCMo"

    # create new user
    client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password},
    )

    # get new access token with fake refresh token
    headers = {"Authorization": f"Bearer {fake_refresh_token}"}
    response = client.post("/api/auth/refresh", headers=headers)

    assert response.status_code == 422


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_logout(client, username, email, password):
    # create new user
    client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password},
    )

    # login
    login_response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    # store access and refresh token
    login_json = login_response.json
    refresh_token = login_json["data"]["refresh_token"]
    access_token = login_json["data"]["access_token"]

    # logout with revoke access token
    headers_access_token = {"Authorization": f"Bearer {access_token}"}
    response_with_access_token = client.delete(
        "/api/auth/logout", headers=headers_access_token
    )

    assert response_with_access_token.status_code == 200

    # logout with revoke refresh token
    headers_refresh_token = {"Authorization": f"Bearer {refresh_token}"}
    response_with_refresh_token = client.delete(
        "/api/auth/logout", headers=headers_refresh_token
    )

    assert response_with_refresh_token.status_code == 200


def test_logout_without_headers(client):
    response = client.delete("/api/auth/logout")

    assert response.status_code == 401


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_logut_with_fake_token(client, username, email, password):
    fake_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDA5MTMxOCwianRpIjoiNDE5NDg1YWYtOTk5Yi00OTEzLWE4ZDctZjdmMGU0NDRlODlmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjk0MDkxMzE4LCJleHAiOjE2OTQwOTMxMTh9.Rm0zvd5IZjEiILRwKuPRCQxN8uH1i77T-HFuDj-H_KA"
    fake_refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDA5MTMxOCwianRpIjoiMDAxNDk0ZjAtNTZjMC00Y2ZlLThkNDMtZTFhOGFmNDI1N2ZmIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTY5NDA5MTMxOCwiZXhwIjoxNjk0Njk2MTE4fQ.zpTdf4CoGx8zEfV4ajrK3q-wwaHBrb9Q_phw9ddkCMo"

    # create new user
    client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password},
    )

    # logout with revoke fake access token
    headers_access_token = {"Authorization": f"Bearer {fake_access_token}"}
    response_with_access_token = client.delete(
        "/api/auth/logout", headers=headers_access_token
    )

    assert response_with_access_token.status_code == 422

    # logout with revoke fake refresh token
    headers_refresh_token = {"Authorization": f"Bearer {fake_refresh_token}"}
    response_with_refresh_token = client.delete(
        "/api/auth/logout", headers=headers_refresh_token
    )

    assert response_with_refresh_token.status_code == 422


@pytest.mark.parametrize(
    "username, email, password",
    [
        ("jhon", "jhon@gmail.com", "jhon"),
        ("doe", "doe@gmail.com", "doe"),
        ("foo", "foo@gmail.com", "foo"),
    ],
)
def test_retrieve_data_from_endpoints_with_jwt_required_using_revoked_access_token(
    client, username, email, password
):
    # create new user
    client.post(
        "/api/users/", json={"username": username, "email": email, "password": password}
    )

    # login and get access token
    login_response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )
    json_login = login_response.json
    access_token = json_login["data"]["access_token"]

    # logout using these access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.delete("/api/auth/logout", headers=headers)

    # retrieve data using revoked access token
    response = client.get("/api/users/me", headers=headers)

    assert response.status_code == 401
