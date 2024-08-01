import jwt 
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from urllib.parse import parse_qs
from authentication.models.User import User

@database_sync_to_async
def get_user(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms=["HS256"])
        user = User.objects.get(id=payload['user_id'])
        return user
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist) as e: 
        return AnonymousUser()

# Custom JWT Authentication Middleware for Channels
class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers']) 
        cookie_bytes = headers[b'cookie']
        cookie_str = cookie_bytes.decode() 
        cookies = cookie_str.split('; ')  
        access_token = None 
        for cookie in cookies:
            if cookie.startswith('accessToken='):
                access_token = cookie[len('accessToken='):]
                break 
            
        if access_token: 
            scope['user'] = await get_user(access_token)
        else:
            scope['user'] = AnonymousUser()
         
        return await super().__call__(scope, receive, send)

def JWTAuthMiddlewareStack(inner):
    return JWTAuthMiddleware(AuthMiddlewareStack(inner))