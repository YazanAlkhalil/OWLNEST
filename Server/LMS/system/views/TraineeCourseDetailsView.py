#DRF
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#serializer
from  system.serializers.TraineeCourseDetailsSerializer import CustomTraineeCourseDetailsSerializer

#models 
from  system.models.Course import Course

#django 
from django.shortcuts import get_object_or_404


class TraineeCourseDetailsView(APIView):
      permission_classes = [IsAuthenticated] 
      def get(self,request,id):
          course = get_object_or_404(Course , id = id)
          enrollment = course.enrollment_set.get(trainee_contract__trainee__user = request.user)
          course = CustomTraineeCourseDetailsSerializer(course , context = {"enrollment":enrollment})
          return Response(course.data)