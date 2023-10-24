from app.core.extensions import ma
from app.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    role = ma.auto_field()


user_schema = UserSchema()
