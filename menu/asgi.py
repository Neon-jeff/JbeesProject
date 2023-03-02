import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path,re_path

from msgresponse.consumers import ResponseConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'menu.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
 

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
   'websocket':AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter([
            re_path('ws/chat/', ResponseConsumer.as_asgi())
        ])
   )
   )
}) 