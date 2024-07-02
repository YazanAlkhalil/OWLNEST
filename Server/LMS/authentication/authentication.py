import jwt,datetime
from rest_framework import exceptions
from django.conf import settings

def createAccessToken(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'ist': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }, 'access_secret', algorithm='HS256')

def decodeAccessToken(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256' )

        return payload['user_id']

    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def createRefreshToken(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'ist': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }, 'refresh_secret', algorithm='HS256')


def decodeRefreshToken(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256' )
        return payload['user_id']

    except:
        raise exceptions.AuthenticationFailed('unauthenticated')