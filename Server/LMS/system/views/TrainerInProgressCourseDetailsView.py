#DRF
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#models 
from system.models.Course  import Course   


#serializer 
from system.serializers.TrainerInProgressCourseDetailsSerializer import TrainerInProgressCourseDetailsSerializer  

#django 
from django.shortcuts import get_object_or_404

class TrainerInProgressCourseDetailsView(generics.RetrieveAPIView):
      serializer_class = TrainerInProgressCourseDetailsSerializer
      permission_classes = [IsAuthenticated]

      def retrieve(self, request, *args, **kwargs):
          course = get_object_or_404(Course , id = kwargs['course_id'])
          serialized_course = TrainerInProgressCourseDetailsSerializer(course)
          return Response(serialized_course.data,200)
      
      

 