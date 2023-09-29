from app.core.extensions import ma
from app.models import Users


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Users

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    role = ma.auto_field()


user_schema = UserSchema()
