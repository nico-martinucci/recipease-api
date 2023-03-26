from flask import Blueprint, jsonify, request
import queries.users as q

users = Blueprint("users", __name__)


@users.route("/signup", methods=["POST"])
def signup_user():
    """Registers a new user."""

    new_user = q.add_new_user(
        username=request.json["username"],
        email=request.json["email"],
        password=request.json["password"],
        first_name=request.json["firstName"],
        last_name=request.json["lastName"],
        bio=request.json["bio"],
    )

    return jsonify(new_user)


@users.route("/login", methods=["POST"])
def login_user():
    """Authenticates an existing user."""

    auth_user = q.authenticate_current_user(
        username=request.json["username"],
        password=request.json["password"]
    )

    return jsonify(auth_user)


@users.route("/photo/<int:user_id>", methods=["POST"])
def add_user_photo(user_id):
    """Adds a new photo for the provided user."""
    # TODO: add after figuring out S3 bucket stuff


@users.route("/", methods=["GET"])
def get_users():
    """Returns list of all users, optionally filtered by username"""

    filter = ""

    if "filter" in request.args:
        filter = request.args["filter"]

    users = q.get_users(filter)

    return jsonify(users)
