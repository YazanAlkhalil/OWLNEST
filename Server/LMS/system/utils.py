from io import BytesIO
from django.template.loader import get_template 
#models
from system.models.Certificate import Certificate
from system.models.Notification import Notification

#serializers 
from system.serializers.NotificationSerializer import NotificationSerializer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# def generate_pdf(path,context):
#     template = get_template(path)
#     html = template.render(context)
#     res = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),res)
#     return res 



 

def send_notification(from_user,to_user,message,company):
          data =  {
               "from_user":from_user.id,
               "to_user": to_user.id,
               "message": message,
               "company":company.id
          }

          notification  = NotificationSerializer(data = data)
          notification.is_valid(raise_exception= True)
          notification.save()
          # Send notification via WebSocket
          channel_layer = get_channel_layer()
          async_to_sync(channel_layer.group_send)(
                f'user_{to_user.id}',
                  {
                      'type': 'send_notification',
                      'message': Notification.objects.filter(to_user=to_user , company = company , is_read = False).count()
                  }
              )