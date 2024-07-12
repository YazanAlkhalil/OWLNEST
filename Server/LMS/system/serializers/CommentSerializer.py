#DRF 
from rest_framework import serializers

#models 
from system.models.Comment import Comment
#django 
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

#serializers 
from system.serializers.ReplySerializer import ReplySerializer

 


class CommentSerializer(serializers.ModelSerializer):
      replies = ReplySerializer(source = "reply_set",read_only = True , many = True)
      class Meta:
          model = Comment
          fields = ["id", "content","replies","likes","dislikes" ]
          extra_kwargs = {"likes":{"read_only": True},"dislikes":{"read_only": True}}

      def to_internal_value(self, data):
           course = data["course"]
           user = data["user"]
           data = super().to_internal_value(data)
           data["course"] = course
           data["user"] = user
           return data
      

      def to_representation(self, instance):
           data = super().to_representation(instance)
           data["likes"] = instance.likes.all().count()
           data["dislikes"] = instance.dislikes.all().count()
           data["username"] = instance.user.username
           data["image"] =None
           if instance.user in instance.likes.all():
                data["reaction"] = 1
           elif instance.user in instance.dislikes.all():
                data["reaction"] = -1
           else :
                data["reaction"] = 0
           return data