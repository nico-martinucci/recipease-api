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


# def verify_jwt(auth):
#     """
#     Takes in a JWT and authenticates it; throws an error if no token or
#     invalid token.
#     """

#     token = auth.split()[1]

#     try:
#         user_auth = jwt.decode(
#             token,
#             os.environ['SECRET_KEY'],
#             algorithms=["HS256"]
#         )
#     except InvalidSignatureError:
#         serialized = {
#             "error": "invalid token"
#         }

#         return jsonify(serialized)
