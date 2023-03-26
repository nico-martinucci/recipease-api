from models import User, db
from flask_bcrypt import Bcrypt
import helpers.tokens as token

bcrypt = Bcrypt()


def add_new_user(username, email, password, first_name, last_name, bio):
    """
    Adds a new user to the database, returning a serialized dictionary if
    successful or error messages if not.
    """

    errors = []

    dupe_username = User.query.get(username)
    # TODO: does this work as .first()?
    dupe_email = User.query.filter(User.email == email).count()

    if dupe_username:
        errors.append("That username is already taken. Please try again.")

    if dupe_email:
        errors.append("That email is already taken. Please try again.")

    if errors:
        return {"error": errors}

    hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

    try:
        new_user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            first_name=first_name,
            last_name=last_name,
            bio=bio
        )

        db.session.add(new_user)
        db.session.commit()

        serialized = {
            "username": new_user.username,
            "email": new_user.email,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "bio": new_user.bio,
        }

        return {"user": serialized}

    except:
        return {"error": "Something went wrong..."}


def authenticate_current_user(username, password):
    """
    Authenticates an existing user, returning a valid JWT if successful or
    error messages if not.
    """

    user = User.query.filter(User.username == username).first()

    if user:
        is_auth = bcrypt.check_password_hash(user.password, password)
        if not is_auth:
            return {"error": "Invalid username/password combination. Please try again."}

        return {"token": token.get_jwt(username)}

    return {"error": "Username not found. Please try again."}


def get_users(filter):
    """
    Queries and returns a list of all users, optionally filtered by the data
    passed to the function.
    """
    filter_term = "%{}%".format(filter)
    users = User.query.filter(User.username.ilike(filter_term)).all()

    serialized = [
        {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "photo_url": user.photo_url
        }
        for user in users
    ]

    return {"users": serialized}
