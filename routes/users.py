from flask import Blueprint, jsonify, request
import queries.users as q

users = Blueprint("users", __name__)


@users.post("/signup")
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


@users.post("/login")
def login_user():
    """Authenticates an existing user."""

    auth_user = q.authenticate_current_user(
        username=request.json["username"],
        password=request.json["password"]
    )

    return jsonify(auth_user)


@users.post("/<username>/photo")
def add_user_photo(username):
    """Adds a new photo for the provided user."""
    # TODO: add after figuring out S3 bucket stuff


@users.get("/")
def get_users():
    """Returns list of all users, optionally filtered by username"""

    users = q.get_users(request.args.get("filter", ""))

    return jsonify(users)


@users.get("/<username>")
def get_user_detail(username):
    """Returns detail for specific user."""

    user = q.get_user(username)

    return jsonify(user)
