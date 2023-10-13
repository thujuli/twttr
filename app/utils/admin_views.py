from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from flask_login import current_user
from flask import redirect


class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect("/login")


class UserView(CustomModelView):
    form_columns = ["username", "email", "password", "role"]
    column_list = ["username", "email", "role", "created", "updated"]
    form_choices = {
        "role": [
            ("user", "USER"),
            ("admin", "ADMIN"),
        ]
    }

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


class TweetView(CustomModelView):
    form_columns = ["user", "content", "image_name", "image_path"]
