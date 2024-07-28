#DRF
from rest_framework.views import APIView
from rest_framework.response import Response 
#models
from system.models.Reply import Reply  
#django 
from django.shortcuts import get_object_or_404





class ReactReplyView(APIView):
        
        def post(self,request,*args,**kwarsg):
            reaction = request.data.get('reaction')
            reply = get_object_or_404(Reply,id = request.data.get('reply'))
            user = request.user
            if reaction == 0 :
              if user in reply.likes.all() :
                  reply.likes.remove(user)
              if user in reply.dislikes.all():
                  reply.dislikes.remove(user)
            if reaction == 1 :
                if user in reply.dislikes.all():
                    reply.dislikes.remove(user)
                if not user in reply.likes.all() :
                    reply.likes.add(user)

            if reaction == -1 :
                if user in reply.likes.all() :
                    reply.likes.remove(user)
                if not user in reply.dislikes.all() :
                    reply.dislikes.add(user)

            return Response({"message":"Reaction updated"},200)
        

