from flask import Blueprint, jsonify, request
import queries.users as q
from helpers import tokens as t, verification as v


users = Blueprint("users", __name__)


@users.post("/signup")
def signup_user():
    """Registers a new user."""

    email = request.json["email"]

    new_user = q.add_new_user(
        username=request.json["username"],
        email=email,
        password=request.json["password"],
        first_name=request.json["firstName"],
        last_name=request.json["lastName"],
        bio=request.json["bio"],
    )

    # FIXME: remove later - just for testing, if above is commented-out to avoid writing to db
    # new_user = {}

    if "error" not in new_user:
        hash = t.get_jwt({"email": email})
        verification_link = "http://www.recipeats.fyi/verify?token=" + hash
        # TODO: uncomment out the below to have verification emails actually be sent
        v.send_verification_email(email=email, link=verification_link)

    return jsonify(new_user)


@users.post("/login")
def login_user():
    """Authenticates an existing user."""

    auth_user = q.authenticate_current_user(
        username=request.json["username"],
        password=request.json["password"]
    )

    return jsonify(auth_user)


@users.post("/verify")
def verify_user():
    """Verifies a new user's e-mail address."""

    token = request.json["token"]

    data = t.verify_jwt(token)

    if "error" in data:
        return jsonify(data)

    username = q.set_user_as_valid(data["email"])
    token = q.get_user_jwt(username, True)

    return jsonify(token)


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


@users.post("/<username>/favorites")
def post_user_favorite(username):
    """Adds a new favorite for the provided user."""

    favorited = q.add_new_user_favorite(
        username=username,
        recipe_id=request.json["recipeId"]
    )

    return jsonify(favorited)


@users.delete("/<username>/favorites/<recipe_id>")
def delete_user_favorite(username, recipe_id):
    """Deletes an existing favorite for the provided user."""

    unfavorited = q.remove_existing_user_favorite(
        username=username,
        recipe_id=recipe_id
    )

    return jsonify(unfavorited)
