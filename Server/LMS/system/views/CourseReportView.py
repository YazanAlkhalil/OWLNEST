#DRF imports 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#django 
from django.shortcuts import get_object_or_404

#serializers 
from system.serializers.CourseReportSerializer import CourseReportSerializer


#models 
from system.models.Course import Course

class CourseReportView(APIView): 
      def get(self,request,*args,**kwargs):
          course = get_object_or_404(Course,id = self.kwargs['id'])
          serialized_data = CourseReportSerializer(data = course)
          serialized_data.is_valid(raise_exception=True)
          return Response(serialized_data.data , status= status.HTTP_200_OK)
          
            