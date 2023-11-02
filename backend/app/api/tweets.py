from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from werkzeug.utils import secure_filename
from flask_cors import CORS
from sqlalchemy.exc import NoResultFound
import os
from app.utils import response
from app.validators.tweet import tweet_validator
from app.services.tweet import TweetCRUD
from app.services.like import like, unlike, get_liked
from app.utils.file import upload_to_minio, allowed_file, get_path

bp = Blueprint("tweets", __name__)
CORS(bp)


@bp.route("/", methods=["POST"])
@jwt_required()
def create_tweet():
    current_user_id = get_jwt_identity()

    # upload file
    if "file" not in request.files:
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
        data.update({"user_id": current_user_id})
        result = TweetCRUD.create(data)

        return response.ok("Tweet has been successfully created", result), 201
        # return response.error("No file part"), 422
    file = request.files["file"]
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == "":
        return response.error("No selected file"), 422

    if file and allowed_file(file.filename):
        content = request.form.get("content")
        image_name = secure_filename(file.filename)
        size = os.fstat(file.fileno()).st_size
        upload_to_minio(image_name, file, size)
        image_path = get_path(image_name, 1)

        # add to database
        data = {
            "user_id": current_user_id,
            "content": content,
            "image_name": image_name,
            "image_path": image_path,
        }
        result = TweetCRUD.create(data)
        return response.ok("Tweet has been successfully created", result), 201
    else:
        return response.error("Something went wrong"), 500


@bp.route("/", methods=["GET"])
@jwt_required()
def get_tweets():
    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", 3)

    try:
        page = int(page)
        per_page = int(per_page)
    except ValueError:
        return response.error("Invalid parameter"), 400

    tweets, total_pages = TweetCRUD.get_all(page, per_page)
    return response.pagination(
        "All tweets have been successfully retrieved", tweets, total_pages
    )


@bp.route("/<int:tweet_id>/likes", methods=["POST"])
@jwt_required()
def liked_tweet(tweet_id):
    current_user_id = get_jwt_identity()

    try:
        TweetCRUD.get_by_id(tweet_id)
    except NoResultFound:
        return response.error("Tweet not found"), 400

    try:
        liked = get_liked(current_user_id, tweet_id)
        unlike(liked)
        return response.ok("Successfully unliked the tweet", {}), 200
    except NoResultFound:
        like(current_user_id, tweet_id)
        return response.ok("Successfully liked the tweet", {}), 200
