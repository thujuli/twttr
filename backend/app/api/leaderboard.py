from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_cors import CORS
from app.utils import response
from app.services.tweet_count import all_tweet_counts

bp = Blueprint("leaderboard", __name__)
CORS(bp)


@bp.route("/", methods=["GET"])
@jwt_required()
def get_count_tweet():
    tweet_counts = all_tweet_counts()
    return response.ok(
        "All tweet counts have been successfully retrieved", tweet_counts
    )
