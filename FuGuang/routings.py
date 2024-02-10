from django.urls import path

from ..Message import consumers

websocket_urlpatterns = [
    path('chat/<str:group_id>/',consumers.ChatConsumer.as_asgi()),
]