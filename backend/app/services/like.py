from app.core.extensions import db
from app.models import Like


def like(user_id: int, tweet_id: int):
    create_like = Like(user_id=user_id, tweet_id=tweet_id)
    db.session.add(create_like)
    db.session.commit()


def get_liked(user_id: int, tweet_id: int):
    return db.session.execute(
        db.select(Like).filter_by(user_id=user_id, tweet_id=tweet_id)
    ).scalar_one()


def unlike(like_instance: Like):
    db.session.delete(like_instance)
    db.session.commit()
