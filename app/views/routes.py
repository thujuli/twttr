from flask import Blueprint, render_template

bp = Blueprint("views", __name__)


@bp.route("/register")
def register():
    return render_template("register.html")


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/")
def home():
    return render_template("index.html")
