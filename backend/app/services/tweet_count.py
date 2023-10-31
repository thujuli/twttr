from app.core.extensions import db
from app.models import TweetCount
from app.schemas.tweet_count import count_tweet_schema


def all_tweet_counts():
    tweets = db.session.execute(
        db.select(TweetCount).order_by(TweetCount.count.desc())
    ).scalars()
    return [count_tweet_schema.dump(tweet) for tweet in tweets]
