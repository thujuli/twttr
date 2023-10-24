from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from app.utils import response
from app.validators.user import user_validator
from app.services.user import UserCRUD

bp = Blueprint("users", __name__)
CORS(bp)


@bp.route("/", methods=["POST"])
def create_user():
    # err, if can't pass json
    json_data = request.get_json()
    if not json_data:
        return response.error("No input data provided"), 400

    # err, if doesn't fit validator fields
    try:
        data = user_validator.load(json_data)
    except ValidationError as err:
        return response.error(err.messages), 422

    # hashing password
    hashed_password = generate_password_hash(data.get("password"))
    data.update({"password": hashed_password})

    try:
        user_by_email = UserCRUD.get_by_email(data.get("email"))
    except NoResultFound:
        result = UserCRUD.create(data)
        return response.ok("User has been added successfully", result), 201

    # if email exist in database, raise err
    if user_by_email:
        return response.error("Email address is already exist"), 409


@bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    data = UserCRUD.get_by_id(current_user_id)

    return response.ok("User has been successfully retrived", data)
