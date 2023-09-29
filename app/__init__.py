from flask import Flask
from app.core.config import Config
from app.core.extensions import db, ma
from app.api.health import bp as bp_health
from app.api.users import bp as bp_users
from app.models import Users, Tweets


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register Blueprint
    app.register_blueprint(bp_health, url_prefix="/api/health")
    app.register_blueprint(bp_users, url_prefix="/api/users")

    # auto create db if no exists
    with app.app_context():
        db.create_all()

    return app
