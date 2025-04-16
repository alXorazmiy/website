from decouple import config
import jwt
import datetime
from rest_framework.exceptions import AuthenticationFailed



JWT_SECRET_KEY = config('MY_SECRET_KEY')

def createToken(user_id):
    payload = {
        'id': user_id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat' : datetime.datetime.utcnow()
    }

    token = jwt.encode(payload=payload, key = JWT_SECRET_KEY, algorithm="HS256")
    return token


def decodeToken(token):
    try:
        payload= jwt.decode(token, JWT_SECRET_KEY, algorithms="HS256")
        return payload['id']
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token muddati tugagan!")
    except jwt.InvalidTokenError:
        raise AuthenticationFailed("Noto'gri token!")
