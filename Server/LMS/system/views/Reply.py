#DRF
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
#serializers
from system.serializers.ReplySerializer import ReplySerializer
#models
from system.models.Comment import Comment 

from system.models.Course import Course
from authentication.models.User import User
#django 
from django.shortcuts import get_object_or_404



class CreateReplyView(CreateAPIView):
      serializer_class = ReplySerializer 
      
      def post(self, request, *args, **kwargs): 
            comment = get_object_or_404(Comment,id = request.data["comment"])
            
            data = {
                  "comment":comment,
                  "user":request.user,
                  "content":request.data["text"]
            }
            serialized_comment = ReplySerializer(data = data)
            serialized_comment.is_valid(raise_exception=True)
            serialized_comment.save()
            return Response(serialized_comment.data)