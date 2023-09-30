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
