from app.core.extensions import db
from app.models import User
from app.schemas.user import user_schema


class UserCRUD:
    @staticmethod
    def get_by_email(email: str):
        return db.session.execute(db.select(User).filter_by(email=email)).scalar_one()

    @staticmethod
    def create(data: dict):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)

    @staticmethod
    def get_by_id(id: int):
        user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
        return user_schema.dump(user)
