from channels.generic.websocket import AsyncWebsocketConsumer
from system.models.Enrollment import Enrollment
from django.utils import timezone
from channels.db import database_sync_to_async


class CalculateTrainingTimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.course_id = self.scope['url_route']['kwargs']['id']
        self.content_id = self.scope['url_route']['kwargs']['content_id']
        self.user = self.scope['user']

        self.enrollment = await self.get_enrollment()

        self.start_time = timezone.now()

        await self.accept()

    async def disconnect(self, close_code):
        end_time = timezone.now()
        time_spent = end_time - self.start_time
        await self.update_training_time(time_spent)

    @database_sync_to_async
    def get_enrollment(self):
        return Enrollment.objects.get(
            trainee_contract__trainee__user=self.user, course__id=self.course_id
        )

    @database_sync_to_async
    def update_training_time(self, time_spent):
        self.enrollment.training_time += time_spent
        self.enrollment.save()

