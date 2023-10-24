from app.core.extensions import db
from app.models import TokenBlocklist
from app.utils import response


def block_token(jti: str, type: str):
    db.session.add(TokenBlocklist(jti=jti, type=type))
    db.session.commit()
    return response.ok(f"{type.capitalize()} token successfully revoked", {})
