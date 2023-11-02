from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.extensions import db


class Tweet(db.Model):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    image_name = Column(String)
    image_path = Column(String)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="tweets")
    likes = relationship("Like", back_populates="tweet")
