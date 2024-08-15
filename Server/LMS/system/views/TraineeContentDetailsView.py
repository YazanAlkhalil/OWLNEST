#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#models
from system.models.Content import Content 

#serializers  
from system.serializers.TestSerializer import TraineeTestSerializer

#django 
from django.shortcuts import get_object_or_404

class TraineeContentDetailsView(APIView):
      permission_classes = [IsAuthenticated]
      def get(self,request,id):
          content = get_object_or_404(Content , id = id)
          if content.is_pdf:
             data = {
                 "title":content.title,
                 "file":request.build_absolute_uri(content.pdf.file_path.url)
             }
             return Response(data,200)
          elif content.is_video:
              data = {
                  "title":content.title,
                  "description":content.video.description,
                  "file":request.build_absolute_uri(content.video.file_path.url)
              }
              return Response(data,200)
          test = TraineeTestSerializer(content.test) 
          data = test.data
          data["title"] = content.title
          return Response(data,200)
       