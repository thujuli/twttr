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
    def get_all(page: int, per_page: int):
        tweets = db.paginate(
            db.select(Tweet).order_by(Tweet.created.desc()),
            page=page,
            per_page=per_page,
        )

        return ([tweet_schema.dump(tweet) for tweet in tweets], tweets.pages)

    @staticmethod
    def get_by_id(id: int):
        return db.session.execute(db.select(Tweet).filter_by(id=id)).scalar_one()
