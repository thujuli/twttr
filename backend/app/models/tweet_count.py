from sqlalchemy import Column, Integer, String
from app.core.extensions import db


class TweetCount(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    count = Column(Integer, default=0)
