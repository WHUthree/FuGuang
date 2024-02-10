from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        self.accept()
        group = self.scope['url_route']['kwargs'].get('group_id')
        async_to_sync(self.channel_layer.group_add)(group,self.channel_name)

    def websocket_receive(self, message):
        group = self.scope['url_route']['kwargs'].get('group_id')
        async_to_sync(self.channel_layer.group_send)(group,{'type':'send.method','message':message})

    def send_method(self,event):
        text = event['message']['text']
        self.send(text)

    def websocket_disconnect(self, message):
        raise StopConsumer()