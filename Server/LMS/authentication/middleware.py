import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get('accessToken')
        print(token)
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                 
                user_id = payload.get('user_id')
                if user_id:
                    try:
                        User = get_user_model()
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
