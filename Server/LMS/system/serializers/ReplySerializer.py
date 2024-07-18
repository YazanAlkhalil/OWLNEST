#DRF 
from rest_framework import serializers

#models 
from system.models.Reply import Reply



class ReplySerializer(serializers.ModelSerializer):

      class Meta:
            model = Reply
            fields = ["id", "content","likes","dislikes"]
            extra_kwargs = {"likes":{"read_only": True},"dislikes":{"read_only": True}}

      def to_internal_value(self, data):
           comment = data["comment"]
           user = data["user"]
           data = super().to_internal_value(data)
           data["comment"] = comment
           data["user"] = user
           return data
      

      def to_representation(self, instance):
           data = super().to_representation(instance)  
           data["likes"] = instance.likes.all().count()
           data["dislikes"] = instance.dislikes.all().count()
           data["username"] = instance.user.username
           data["image"] =instance.user.image.url if instance.user.image else None
           if instance.user in instance.likes.all():
                data["reaction"] = 1
           elif instance.user in instance.dislikes.all():
                data["reaction"] = -1
           else :
                data["reaction"] = 0
           return data