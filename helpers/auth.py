from os import environ
from functools import wraps
from flask import abort, request
import jwt

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'Authorization' in request.headers:
            print("line 10")
            abort(401)

        user = None
        data = request.headers['Authorization'].encode('ascii','ignore')
        print(data)
        token = data.decode("utf-8")
        print(token)
        try:
            print("line 17")
            user = jwt.decode(token, environ.get("SECRET_KEY"), algorithms=["HS256"])
        except:
            abort(401)

        return f(*args, **kws)            
    return decorated_function