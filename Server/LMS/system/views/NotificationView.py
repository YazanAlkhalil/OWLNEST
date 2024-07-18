#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
#serializers
from system.serializers.NotificationSerializer import NotificationSerializer

#models 
from system.models.Notification import Notification

class NotificationList(APIView):

      def get(self,requset,*args,**kwargs):
          notifications = Notification.objects.filter(to_user = requset.user ,  company__id = kwargs['id'])
    
          for notification in notifications :
                notification.is_read = True
                notification.save()
          
          serialized_notify = NotificationSerializer(notifications,many =True)
          return Response(serialized_notify.data , 200)