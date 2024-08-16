#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#models
from system.models.DraftContent import DraftContent
from system.models.DraftPDF import DraftPDF
from system.models.DraftVideo import DraftVideo
from system.models.DraftTest import DraftTest

#serializers 
from system.serializers.DraftTestSerializer import DraftTestSerializer
#django 
from django.shortcuts import get_object_or_404

class TrainerRetrieveContentView(APIView):
      permission_classes = [IsAuthenticated]
      def get(self,request,id):
          content = get_object_or_404(DraftContent , id = id)
          if content.is_pdf:
             data = {
                 "title":content.title,
                 "file":request.build_absolute_uri(content.draftpdf.file.url)
             }
             return Response(data,200)
          elif content.is_video:
              data = {
                  "title":content.title,
                  "description":content.draftvideo.description,
                  "file":request.build_absolute_uri(content.draftvideo.file.url)
              }
              return Response(data,200)
          test = DraftTestSerializer(content.drafttest) 
          data = test.data
          data["title"] = content.title
          return Response(data,200)
      
      def delete(self,request,id):
          content = get_object_or_404(DraftContent , id = id)
          content.delete()
          return Response({"message":"the content deleted successfully"},204)