from app.core.extensions import ma
from app.schemas.user import UserSchema
from app.models import Tweet


class TweetSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tweet

    id = ma.auto_field()
    content = ma.auto_field()
    image_name = ma.auto_field()
    image_path = ma.auto_field()
    user = ma.Nested(UserSchema)


tweet_schema = TweetSchema()
