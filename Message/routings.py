from django.urls import path

from message import consumers

websocket_urlpatterns = [
    path('chat/<int:group_id>/', consumers.ChatConsumer.as_asgi()),
]