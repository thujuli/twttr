import pytest


# @pytest.mark.parametrize(
#     "username, email, password, role",
#     [
#         ("jhon", "jhon@gmail.com", "jhon", "admin"),
#         ("ucup", "ucup@gmail.com", "ucup", "user"),
#         ("asep", "asep@gmail.com", "asep", "user"),
#     ],
# )
# def test_create_user(client, username, email, password, role):
#     response = client.post(
#         "/api/users/",
#         json={"username": username, "email": email, "password": password, "role": role},
#     )

#     assert response.status_code == 201


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
