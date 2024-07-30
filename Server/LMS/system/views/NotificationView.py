#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
#serializers
from system.serializers.NotificationSerializer import NotificationSerializer

#models 
from system.models.Notification import Notification

class NotificationList(APIView):

      def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(to_user=request.user, company__id=kwargs['id'])
        serialized_notify = NotificationSerializer(notifications, many=True)

        response = Response(serialized_notify.data, status=200)

        # Mark notifications as read after response is prepared
        for notification in notifications:
            notification.is_read = True
            notification.save()
z 
        return response