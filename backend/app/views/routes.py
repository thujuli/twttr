from flask import Blueprint, redirect, render_template

bp = Blueprint("views", __name__)


@bp.route("/register")
def register():
    return render_template("auth/register.html")


@bp.route("/login")
def login():
    return render_template("auth/login.html")


@bp.route("/")
def home():
    return redirect("/login")
