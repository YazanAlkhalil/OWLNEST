# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer , WebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from system.models.Notification import Notification

User = get_user_model()

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_anonymous:
            await self.close()
        else:
            self.group_name = f'user_{self.user.id}'
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()
            print("CONSUMER",self.group_name)
            
            company = self.scope['url_route']['kwargs']['id']
            # Send unread notifications 
            await self.send(text_data=json.dumps({
                    'message': await self.get_unread_notifications(self.user , company)
            })) 
               

    async def disconnect(self, close_code):
        if not self.user.is_anonymous:
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_notification',
                'message': data['message']
            }
        )

    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def get_unread_notifications(self, user , company):
        notifications_number = Notification.objects.filter(to_user=user , company = company , is_read = False).count()
        return notifications_number

 