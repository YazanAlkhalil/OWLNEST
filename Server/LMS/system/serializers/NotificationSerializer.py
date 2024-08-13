#DRF 
from rest_framework import serializers
from rest_framework import serializers
from system.models.Notification import Notification

class NotificationSerializer(serializers.ModelSerializer):
      time_since_sent = serializers.SerializerMethodField(read_only = True)
      username = serializers.CharField(source = "from_user.username" , read_only = True)
      image = serializers.CharField(source = "from_user.image",read_only = True)
      class Meta:
          model = Notification
          fields = ['id', 'username', 'image','from_user','to_user', 'message', 'is_read', 'time_since_sent',"company"]
          extra_kwargs = {
              "from_user":{
                  "write_only":True
              },
              "to_user":{
                  "write_only":True
              },
              "is_read":{
                  "read_only":True
              },
              "company":{
                  "write_only":True
              }
          }

      def get_time_since_sent(self, obj):
          time_diff = obj.time_since_sent()
          days = time_diff.days
          hours, remainder = divmod(time_diff.seconds, 3600)
          minutes, seconds = divmod(remainder, 60)
          if days > 0:
              return f"{days} days"
          elif hours > 0:
              return f"{hours} hours"
          elif minutes > 0:
              return f"{minutes} minutes"
          else:
              return f"{seconds} seconds"
          
 