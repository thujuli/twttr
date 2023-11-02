from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_login import UserMixin
from app.core.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, server_default="user")
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now())

    tweets = relationship("Tweet", back_populates="user")
    likes = relationship("Like", back_populates="user")

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_role(self, role_name):
        return self.role == role_name
