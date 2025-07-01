from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "posts_updates"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "WebSocket connected!"
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            "message": "Echo: " + text_data
        }))

    # Method to receive broadcasted messages
    async def send_new_post(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
