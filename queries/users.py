from models import User, db
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

bcrypt = Bcrypt()


def add_new_user(username, email, password, first_name, last_name, bio):
    """Adds a new user to the database."""

    errors = []

    dupe_username = User.query.get(username)
    dupe_email = User.query.filter(User.email == email).count()

    print("DUPE_USERNAME", dupe_username)
    print("DUPE_EMAIL", dupe_email)

    if dupe_username:
        errors.append("That username is already taken. Please try again.")

    if dupe_email:
        errors.append("That email is already taken. Please try again.")

    if errors:
        return {"error": errors}

    hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

    try:
        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            first_name=first_name,
            last_name=last_name,
            bio=bio
        )

        db.session.add(user)
        db.session.commit()

        serialized = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "bio": user.bio,
        }

        return {"user": serialized}

    except:
        return {"error": "Something went wrong..."}


def authenticate_current_user():
    """Authenticates an existing user."""
