from flask import Blueprint

users = Blueprint("users", __name__)


@users.route("/signup", methods=["POST"])
def signup_user():
    """Registers a new user"""

    return {"message": "users!"}
