from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_login import LoginManager
from app.admin.base import HomeAdminView


db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
admin_panel = Admin(
    name="Admin Panel",
    template_mode="bootstrap4",
    index_view=HomeAdminView(),
)
login_manager = LoginManager()
