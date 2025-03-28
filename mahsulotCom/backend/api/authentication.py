import jwt
import datetime
from rest_framework.exceptions import AuthenticationFailed





def create_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat' : datetime.datetime.utcnow()

        }, 'access_secret', algorithm='HS256'
    )

def decode_token(token):
    try:
        user_id = jwt.decode(token, 'access_secret', algorithms = 'HS256')
        return user_id["user_id"]
    except:
        raise AuthenticationFailed("Error")