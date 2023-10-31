from flask import Flask
from app.core.config import Config
from app.core.extensions import db, ma, jwt, admin_panel, login_manager
from app.api.health import bp as bp_health
from app.api.users import bp as bp_users
from app.api.auth import bp as bp_auth
from app.api.tweets import bp as bp_tweets
from app.api.leaderboard import bp as bp_leaderboard
from app.views.routes import bp as bp_views
from app.models import User, Tweet, TokenBlocklist, TweetCount
from app.admin.user import UserView
from app.admin.tweet import TweetView
from app.utils.login import load_user
from app.utils.celery_app import celery_init_app
from app.tasks import tweet
from app.utils.schedulers import schedule


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://redis",
            result_backend="redis://redis",
            enable_utc=False,
            timezone="Asia/Makassar",
            task_ignore_result=True,
            beat_schedule={
                schedule[0]["name"]: schedule[0]["desc"],
                schedule[1]["name"]: schedule[1]["desc"],
            },
        ),
    )

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    admin_panel.init_app(app)
    login_manager.init_app(app)
    celery_init_app(app)

    # Register Blueprint
    app.register_blueprint(bp_health, url_prefix="/api/health")
    app.register_blueprint(bp_users, url_prefix="/api/users")
    app.register_blueprint(bp_auth, url_prefix="/api/auth")
    app.register_blueprint(bp_tweets, url_prefix="/api/tweets")
    app.register_blueprint(bp_leaderboard, url_prefix="/api/leaderboard")
    app.register_blueprint(bp_views, url_prefix="")

    # Add admin model view
    admin_panel.add_view(UserView(User, db.session))
    admin_panel.add_view(TweetView(Tweet, db.session))

    # auto create db if no exists
    with app.app_context():
        db.create_all()

    return app
