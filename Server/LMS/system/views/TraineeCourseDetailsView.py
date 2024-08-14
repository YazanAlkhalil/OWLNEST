#DRF
from rest_framework.views import APIView

from rest_framework.response import Response
#serializer
from  system.serializers.TraineeCourseDetailsSerializer import TraineeCourseDetailsSerializer

#models 
from  system.models.Course import Course

#django 
from django.shortcuts import get_object_or_404


class TraineeCourseDetailsView(APIView): 
      def get(self,request,course_id):
          course = get_object_or_404(Course , id = course_id)
          course = TraineeCourseDetailsSerializer(course)
          return Response(course.data)