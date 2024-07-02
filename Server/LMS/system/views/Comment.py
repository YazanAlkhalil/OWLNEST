#DRF
from rest_framework.generics import ListCreateAPIView
#serializers
from system.serializers.CommentSerializer import CommentSerializer
#models
from system.models.Comment import Comment 

class ListCreateCommentView(ListCreateAPIView):
      serializer_class = CommentSerializer
      queryset = Comment.objects.all() 
 

      