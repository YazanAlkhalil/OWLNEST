import jwt,datetime
from rest_framework import exceptions
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings 
from authentication.models import User

from rest_framework.authentication import BaseAuthentication
def createAccessToken(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'ist': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }, 'access_secret', algorithm='HS256')

def decodeAccessToken(token):
    try: 
        payload = jwt.decode(token,'access_secret',algorithms=['HS256'])
        print(payload)
        return payload['user_id']

    except Exception as e:
        print(e)
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
    


class JWTAuthenticationBackEnd(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('accessToken')   
        if token:
            try: 
                payload = jwt.decode(token, 'access_secret', algorithms=['HS256'])
                user_id = payload['user_id']
                try:
                    user = User.objects.get(id=user_id) 
                    request.user = user   
                except User.DoesNotExist:
                    request.user = None   

            except jwt.ExpiredSignatureError:
                request.user = None   
            except jwt.InvalidTokenError:
                request.user = None  
        else:
            request.user = None    

        return (request.user,None)
    

class JWTAuthenticationBackEnd(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('accessToken')
        if not token:
            return None
        
        try:
            payload = jwt.decode(token, 'access_secret', algorithms=['HS256'])
            user_id = payload['user_id']
            try:
                user = User.objects.get(id=user_id)
                return (user, None)
            except User.DoesNotExist:
                return None
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None