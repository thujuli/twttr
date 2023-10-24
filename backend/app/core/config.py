import os
from datetime import timedelta

JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES_MINUTES", "30"))
JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES_DAYS", "7"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRES)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=JWT_REFRESH_TOKEN_EXPIRES)
