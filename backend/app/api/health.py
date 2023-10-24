from flask import Blueprint
from flask_cors import CORS

bp = Blueprint("health", __name__)
CORS(bp)


@bp.route("/", methods=["GET"])
def health_check():
    return {"status": "ok"}
