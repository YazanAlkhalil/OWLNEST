#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
#serializers
from system.serializers.CommentSerializer import CommentSerializer
#models
from system.models.Comment import Comment 

from system.models.Course import Course
from authentication.models.User import User
#django 
from django.shortcuts import get_object_or_404





class ReactCommentView(APIView):
        
        def post(self,request,*args,**kwarsg):
            reaction = request.data.get('reaction')
            comment = get_object_or_404(Comment,id = request.data.get('comment'))
            user = request.user
            if reaction == 0 :
              if user in comment.likes.all() :
                  comment.likes.remove(user)
              if user in comment.dislikes.all():
                  comment.dislikes.remove(user)
            if reaction == 1 :
                if user in comment.dislikes.all():
                    comment.dislikes.remove(user)
                if not user in comment.likes.all() :
                    comment.likes.add(user)

            if reaction == -1 :
                if user in comment.likes.all() :
                    comment.likes.remove(user)
                if not user in comment.dislikes.all() :
                    comment.dislikes.add(user)

            return Response({"message":"Reaction updated"},200)
        

