from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.extensions import db


class Like(db.Model):
    __tablename__ = "likes"

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    tweet_id = Column(
        Integer, ForeignKey("tweets.id", ondelete="CASCADE"), primary_key=True
    )

    tweet = relationship("Tweet", back_populates="likes")
    user = relationship("User", back_populates="likes")
