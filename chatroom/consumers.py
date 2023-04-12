import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chatroom.models import ChatRoomMessageModel


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        payload = {
            "type": "chat_message",
            "message": message,
        }

        await database_sync_to_async(self.save_message)(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            payload
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    'message': message
                }
            )
        )

    def save_message(self, message):
        ChatRoomMessageModel.objects.create(
            group_name=self.room_name,
            message=message
        )
