import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DeviceUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def device_update_notification(self, event):
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
