from flask import Blueprint, jsonify, request
import queries.users as q

users = Blueprint("users", __name__)


@users.route("/signup", methods=["POST"])
def signup_user():
    """Registers a new user"""

    new_user = q.add_new_user(
        username=request.json["username"],
        email=request.json["email"],
        password=request.json["password"],
        first_name=request.json["firstName"],
        last_name=request.json["lastName"],
        bio=request.json["bio"],
    )

    return jsonify(new_user)
