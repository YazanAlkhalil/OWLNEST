#DRF
from rest_framework.generics import ListCreateAPIView , CreateAPIView
from rest_framework.generics import ListCreateAPIView , CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs['id'])
        return course.comment_set.all()

    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs['id'])
        data = {
            "course": course,   
            "user": request.user,  
            "content": request.data.get("text")
        }
        serialized_comment = self.get_serializer(data=data, context={'request': request})
        serialized_comment.is_valid(raise_exception=True)
        serialized_comment.save()  
        return Response(serialized_comment.data)