from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.security import check_password_hash
from sqlalchemy.exc import NoResultFound
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from flask_login import login_user, logout_user
from flask_cors import CORS
from app.utils import response
from app.validators.auth import login_validator
from app.services.user import UserCRUD
from app.services.token import block_token

# must be imported, used by flask-jwt-extended
from app.core.security import check_if_token_revoked


bp = Blueprint("auth", __name__)
CORS(bp)


@bp.route("/login", methods=["POST"])
def login():
    # err, if can't pass json
    json_data = request.get_json()
    if not json_data:
        return response.error("No input data provided"), 400

    # err, if doesn't fit validator fields
    try:
        data = login_validator.load(json_data)
    except ValidationError as err:
        return response.error(err.messages), 422

    try:
        user_by_email = UserCRUD.get_by_email(data.get("email"))
        login_user(user_by_email)
    except NoResultFound:
        return response.error("Incorrect Email or Password"), 401

    # err, if password not match
    if not check_password_hash(user_by_email.password, data.get("password")):
        return response.error("Incorrect Email or Password"), 401

    access_token = create_access_token(identity=user_by_email.id)
    refresh_token = create_refresh_token(identity=user_by_email.id)
    res = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user_id": user_by_email.id,
    }

    return response.ok("Successfully Login", res)


@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    access_token = create_access_token(identity=current_user_id)
    return response.ok(
        "Successfully refreshing token",
        {"access_token": access_token, "user_id": current_user_id},
    )


@bp.route("/logout", methods=["DELETE"])
@jwt_required(verify_type=False)
def modify_token():
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    logout_user()

    return block_token(jti, ttype)
