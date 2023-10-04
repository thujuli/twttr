import pytest
from datetime import timedelta
from app import create_app
from app.core.extensions import db


class ConfigTest:
    SECRET_KEY = "123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "123"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)


@pytest.fixture()
def app():
    app = create_app(config_class=ConfigTest)

    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def access_token_jhon(client):
    username = "jhon"
    email = "jhon@gmail.com"
    password = "jhon"
    role = "user"

    # create new user
    client.post(
        "/api/users/",
        json={"username": username, "email": email, "password": password, "role": role},
    )

    # login
    login_response = client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    login_json = login_response.json
    return login_json["data"]["access_token"]


@pytest.fixture()
def tweets_jhon(client, access_token_jhon):
    headers = {"Authorization": f"Bearer {access_token_jhon}"}

    tweets = [
        {"content": "Hello World"},
        {"content": "Flask"},
        {"content": "Web Framework"},
    ]

    # add new tweet
    for tweet in tweets:
        client.post("/api/tweets/", headers=headers, json={"content": tweet["content"]})
