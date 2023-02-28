from channels.generic.websocket import AsyncWebsocketConsumer,JsonWebsocketConsumer,AsyncConsumer
import json
from channels.exceptions import StopConsumer

class ResponseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name='chatroom'
        self.room_group_name='chat' + self.room_name
        await self.accept()
        await self.send(text_data='Hello World')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json=json.loads(text_data)
            message=text_data_json['message']
            sender=text_data_json['sender']
            time=text_data_json['time']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                'type':'chat_message',
                'message':message,
                'sender':sender,
                'time':time
                }
                )
    async def chat_message(self,event):
        message=event['message']
        sender=event['sender']
        time=event['time']
        await self.send(text_data=json.dumps({
            'message':message,
            'sender':sender,
            'time':time
        }))
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )