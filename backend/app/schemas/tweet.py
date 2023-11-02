from app.core.extensions import ma
from app.schemas.user import UserSchema
from app.schemas.like import LikeSchema
from app.models import Tweet


class TweetSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tweet

    id = ma.auto_field()
    content = ma.auto_field()
    image_name = ma.auto_field()
    image_path = ma.auto_field()
    user = ma.Nested(UserSchema)
    likes = ma.Pluck(LikeSchema, "user_id", many=True)


tweet_schema = TweetSchema()
