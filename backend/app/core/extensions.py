from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_login import LoginManager


db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
admin_panel = Admin()
login_manager = LoginManager()
