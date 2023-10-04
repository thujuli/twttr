from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.utils import response
from app.validators.tweet import tweet_validator
from app.services.tweet import TweetCRUD
from app.schemas.tweet import tweet_schema

bp = Blueprint("tweets", __name__)


@bp.route("/", methods=["POST"])
@jwt_required()
def create_tweet():
    # err, if can't pass json
    json_data = request.get_json()
    if not json_data:
        return response.error("No input data provided"), 400

    # err, if doesn't fit validator fields
    try:
        data = tweet_validator.load(json_data)
    except ValidationError as err:
        return response.error(err.messages), 422

    # add current user id to data
    current_user_id = get_jwt_identity()
    data.update({"user_id": current_user_id})
    result = TweetCRUD.create(data)

    return response.ok("Tweet has been successfully created", result), 201


@bp.route("/", methods=["GET"])
@jwt_required()
def get_tweets():
    tweets = TweetCRUD.get_all()
    return response.ok("All tweets have been successfully retrieved", tweets)
