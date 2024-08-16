#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#models
from system.models.Course import Course

#serializers
from system.serializers.CourseInfoSerializer import CourseInfoSerializer


class CourseInfoView(APIView):
      permission_classes = [IsAuthenticated]
      def get(self, request,id):
            try:
              course = Course.objects.get(id = id)
            except Course.DoesNotExist:
                 return Response({"message":"Course Doesnt Exists"},404)
            
            serialized_course = CourseInfoSerializer(course,context = {'request':request}) 
            return Response(serialized_course.data)