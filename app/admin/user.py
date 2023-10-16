from app.admin.base import CustomModelView
from werkzeug.security import generate_password_hash


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
