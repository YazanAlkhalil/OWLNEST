# your_app/routing.py
from django.urls import path
from system.consumers.NotificationConsumer import NotificationConsumer
from system.consumers.CalculateTrainingTimeConsumer import CalculateTrainingTimeConsumer

websocket_urlpatterns = [
    path('ws/company/<id>/notification/', NotificationConsumer.as_asgi()), 
    path('ws/course/<id>/content/<content_id>',CalculateTrainingTimeConsumer.as_asgi())
]
