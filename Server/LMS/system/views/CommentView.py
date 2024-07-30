#DRF
from rest_framework.generics import ListCreateAPIView , CreateAPIView
from rest_framework.generics import ListCreateAPIView , CreateAPIView
from rest_framework.response import Response
#serializers
from system.serializers.CommentSerializer import CommentSerializer
#models
from system.models.Comment import Comment 

from system.models.Course import Course
from authentication.models.User import User
#django 
from django.shortcuts import get_object_or_404



class ListCreateCommentView(ListCreateAPIView):
      serializer_class = CommentSerializer
      queryset = Comment.objects.all() 
 

      def post(self, request, *args, **kwargs):
            course = get_object_or_404(Course,id = kwargs['id'])
            data = {
                  "course":course,
                  "user":request.user,
                  "content":request.data["text"]
            }
            serialized_comment = CommentSerializer(data = data)
            serialized_comment.is_valid(raise_exception=True)
            return Response(serialized_comment.data) 
       