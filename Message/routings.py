from django.urls import path

from Message import consumers

websocket_urlpatterns = [
    path('chat/<int:group_id>/',consumers.ChatConsumer.as_asgi()),
]