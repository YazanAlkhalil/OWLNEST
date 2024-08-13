#DRF
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.DraftUnit import DraftUnit 
#serializer 
from system.serializers.DraftContentSerializer import DraftContentserializer
from system.serializers.DraftPDFSerializer import DraftPDFSerializer
from system.serializers.DraftVideoSerializer import DraftVideoSerializer
#django 
from django.shortcuts import get_object_or_404

class AddContentToUnit(CreateAPIView):
      serializer_class = DraftContentserializer
      permission_classes = [IsAuthenticated]

      def post(self, request, *args, **kwargs):
          if not( "title" in request.data.keys()):
              raise ValidationError({"message":"Please Enter the content title"}) 
          if not( "order" in request.data.keys()):
               raise ValidationError({"message":"Please Enter the content order"}) 
          if not( "type" in request.data.keys()):
               raise ValidationError({"message":"Please Enter the content type"})
          unit = get_object_or_404(DraftUnit,id = kwargs["unit_id"])
          type = request.data["type"]
          data = {
                  "title":request.data["title"],
                  "order":request.data["order"],
                   
             }
          if type.lower() == "pdf": 
             serialized_content = DraftContentserializer(data = data)
             serialized_content.is_valid(raise_exception=True)
             content = serialized_content.save(unit = unit,is_pdf = True)
             pdf_data = {
                  "file":request.data["file"]
             }
             serialized_pdf = DraftPDFSerializer(data = pdf_data)
             serialized_pdf.is_valid(raise_exception=True)
             serialized_pdf.save(content = content)
             return Response({"message":"the pdf uploaded successfully"},201)
          
          if type.lower() == "video":
             serialized_content = DraftContentserializer(data = data)
             serialized_content.is_valid(raise_exception=True)
             content = serialized_content.save(unit = unit,is_video = True)
             pdf_data = {
                  "file":request.data["file"]
             }
             serialized_pdf = DraftVideoSerializer(data = pdf_data)
             serialized_pdf.is_valid(raise_exception=True)
             serialized_pdf.save(content = content)
             return Response({"message":"the video uploaded successfully"},201)
          if type.lower() == "test":
              pass

             
               

