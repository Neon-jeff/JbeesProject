from django.urls import path
from .consumers import ResponseConsumer


websocket_urlpatterns=[
    path('ws/chat/',ResponseConsumer.as_asgi())
]