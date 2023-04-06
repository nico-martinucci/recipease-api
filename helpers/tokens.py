from os import environ
import jwt
from jwt.exceptions import InvalidSignatureError


def get_jwt(data):
    """Accepts a dictionary of data and generates and returns a valid JWT."""

    new_jwt = jwt.encode(
        data,
        environ.get("SECRET_KEY"),
        algorithm="HS256"
    )

    return new_jwt


def verify_jwt(token):
    """
    Takes in a JWT and authenticates it; throws an error if no token or
    invalid token.
    """

    serialized = None

    try:
        data = jwt.decode(
            token,
            environ.get("SECRET_KEY"),
            algorithms=["HS256"]
        )

        serialized = data
    except InvalidSignatureError:
        serialized = {"error": "invalid token"}

    return serialized
