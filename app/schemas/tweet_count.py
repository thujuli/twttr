from app.core.extensions import ma
from app.models import TweetCount


class CountTweetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TweetCount


count_tweet_schema = CountTweetSchema()
