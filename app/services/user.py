from app.core.extensions import db
from app.models import Users
from app.schemas.user import user_schema


class UserCRUD:
    @staticmethod
    def get_by_email(email: str):
        return db.session.execute(db.select(Users).filter_by(email=email)).scalar_one()

    @staticmethod
    def create(data: dict):
        user = Users(**data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
