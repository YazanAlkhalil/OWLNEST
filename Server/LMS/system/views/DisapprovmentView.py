#DRF
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
 
#models 
from system.models.Company import Company
from system.models.Course import Course
from system.models.Notification import Notification

#serializers 
from system.serializers.NotificationSerializer import NotificationSerializer
#django 
from django.shortcuts import get_object_or_404

#channels  
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



class DisapprovmentView(DestroyAPIView): 
      permission_classes = [IsAuthenticated]
      def destroy(self, request, *args, **kwargs):
          if not "reason" in request.data.keys():
               return Response({"message":"please add reason for notify trainers"}) 
          company = get_object_or_404(Company,id  = kwargs["company_id"])
          course = get_object_or_404(Course , id = kwargs["course_id"])
          approvemnet = self.request.user.admin.admin_contract_set.get(company = company).adminapprovment_set.get(course=course)
          approvemnet.delete()
          reason = request.data["reason"]
          for trainer in course.trainers.all():
              if trainer.trainer.user == request.user :
                   continue
              data =  {
                  "from_user":request.user.id,
                  "to_user": trainer.trainer.user.id,
                  "message": f"{course.name}:Disapprovment\t Reason : {reason}" ,
                  "company": company.id
              }

              notification  = NotificationSerializer(data = data)
              notification.is_valid(raise_exception= True)
              notification.save()
              # Send notification via WebSocket
              channel_layer = get_channel_layer()
              async_to_sync(channel_layer.group_send)(
                    f'user_{trainer.trainer.user.id}',
                      {
                          'type': 'send_notification',
                          'message': Notification.objects.filter(to_user=trainer.trainer.user , company = course.company , is_read = False).count()
                      }
                  )
              

              return Response({"message":"the course disapproved"},204)