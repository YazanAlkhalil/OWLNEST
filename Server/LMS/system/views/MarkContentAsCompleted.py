#DRF 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
#models 
from system.models.Finished_Content import Finished_Content
from system.models.Finished_Unit import Finished_Unit
from system.models.Enrollment import Enrollment
from system.models.Content import Content
#serializers 
from system.serializers.MarkContentSerializer import MarkContentSerializer

#django
from django.shortcuts import get_object_or_404

class MarkContentView(CreateAPIView):
      serializer_class = MarkContentSerializer
      def post(self, request, *args, **kwargs):
     
          enrollment =  get_object_or_404(Enrollment,trainee_contract__trainee__user = request.user)
          content = get_object_or_404(Content,content = request.data["content"])
          if enrollment.course != content.unit.course :
               return Response({"message":"you can't mark content if you are not enroll in this course"},status.HTTP_400_BAD_REQUEST)
          data = {
               'enrollment':enrollment,
               'content':content,
               'xp': 100
          }
          serialized_data = MarkContentSerializer(data = data)
          serialized_data.is_valid(raise_exception= True)
          serialized_data.save()
          return Response({"message":"the content marked as complete"},status.HTTP_200_OK)
