from app.core.extensions import db
from app.models import Tweet
from app.schemas.tweet import tweet_schema


class TweetCRUD:
    @staticmethod
    def create(data: dict):
        tweet = Tweet(**data)
        db.session.add(tweet)
        db.session.commit()
        return tweet_schema.dump(tweet)

    @staticmethod
    def get_all():
        tweets = db.session.execute(
            db.select(Tweet).order_by(Tweet.created.desc())
        ).scalars()
        return [tweet_schema.dump(tweet) for tweet in tweets]
