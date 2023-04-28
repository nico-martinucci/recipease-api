from os import environ
from functools import wraps
from flask import abort, request
import jwt


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'Authorization' in request.headers:
            abort(401)

        user = None
        data = request.headers['Authorization'].encode('ascii', 'ignore')
        token = data.decode("utf-8")
        try:
            user = jwt.decode(token, environ.get(
                "SECRET_KEY"), algorithms=["HS256"])
        except:
            abort(401)

        return f(*args, **kws)
    return decorated_function
