import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter,get_default_application
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path,re_path
# from asgiref import headers
from msgresponse.consumers import ResponseConsumer



# def cors_middleware(get_response):
#     async def middleware(scope, receive, send):
#         response = await get_response(scope, receive, send)

#         asgi_add_header(response, b'access-control-allow-origin', b'*')
#         asgi_add_header(response, b'access-control-allow-headers', b'*')

#         return response

#     return middleware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'menu.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
   'websocket':AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter([
            re_path('ws/chat/', ResponseConsumer.as_asgi())
        ])
   )
   )
})
# application = cors_middleware(application)
