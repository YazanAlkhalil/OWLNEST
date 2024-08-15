#DRF
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.Course import Course
from system.models.DraftAdditionalResources import DraftAdditionalResources
#serializer
from system.serializers.DraftAdditionalResourcesSerializer import DraftAdditionalResourcesSerializer

#django 
from django.shortcuts import get_object_or_404

class AddAdditionalResourcesToCourse(ListCreateAPIView):
      serializer_class = DraftAdditionalResourcesSerializer
      permission_classes = [IsAuthenticated] 

      def get(self, request, *args, **kwargs):
              draft_additonal = DraftAdditionalResources.objects.get(course__id = self.kwargs["id"])
              serialized_draft_additonal = self.serializer_class(draft_additonal)
              return Response(serialized_draft_additonal.data,200)
      
      def post(self, request, *args, **kwargs):
          
          if not( "text" in request.data.keys()):
              raise ValidationError({"message":"Please Enter the additonal resources as text"})  
          course =get_object_or_404(Course,id =  kwargs["id"])
          if course.draftadditionalresources : 
               course.draftadditionalresources.delete()
          resource_data = {
               "text":request.data.get('text')
          }

          serialized_resource = DraftAdditionalResourcesSerializer(data = resource_data)
          serialized_resource.is_valid(raise_exception=True)
          serialized_resource.save(course = course)



          return Response({"message":"additional resources added to the course"})
      

