"""
ASGI config for LMS project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#channels
from channels.routing import ProtocolTypeRouter, URLRouter
import system.routing
from system.WebSocketMiddleWare import JWTAuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTAuthMiddlewareStack(
        URLRouter(
            system.routing.websocket_urlpatterns
        )
    ),
})