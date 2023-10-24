from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.extensions import db


class TokenBlocklist(db.Model):
    id = Column(Integer, primary_key=True)
    jti = Column(String(36), nullable=False, index=True)
    type = Column(String(16), nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
