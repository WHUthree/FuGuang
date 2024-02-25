from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import datetime

from square.models import MealInfo

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        group = self.scope['url_route']['kwargs'].get('group_id')
        disconn_time = MealInfo.objects.get(MealInfo_id=group).meal_time + datetime.timedelta(hours=3)
        if (datetime.datetime.now() > disconn_time):
            raise ConnectionRefusedError("this chat room is overdue")
        else:
            self.accept()
            async_to_sync(self.channel_layer.group_add)(group, self.channel_name)

    def websocket_receive(self, message):
        group = self.scope['url_route']['kwargs'].get('group_id')
        async_to_sync(self.channel_layer.group_send)(group, {'type': 'send.method', 'message': message})

    def send_method(self, event):
        text = event['message']['text']
        self.send(text)

    def websocket_disconnect(self, message):
        raise StopConsumer()
