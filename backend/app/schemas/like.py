from app.core.extensions import ma
from app.models import Like


class LikeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Like

    user_id = ma.auto_field()
    tweet_id = ma.auto_field()


# class UserSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = User
#
#     id = ma.auto_field()
#     username = ma.auto_field()
#     email = ma.auto_field()
#     role = ma.auto_field()

like_schema = LikeSchema()
