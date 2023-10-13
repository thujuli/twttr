from app.core.extensions import login_manager
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
