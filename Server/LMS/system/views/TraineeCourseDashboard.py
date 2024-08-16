#DRF  
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
#django 
from django.shortcuts import get_object_or_404

#serializers 
from system.serializers.TraineeCourseDashboardSerializer import TraineeCourseDashboardSerializer

#models 
from system.models.Enrollment import Enrollment
from system.models.Course import Course

class TraineeCourseDashboard(APIView):
      permission_classes = [IsAuthenticated]
      def get(self, request, *args, **kwargs):
          course = get_object_or_404(Course, id=self.kwargs['id'])
          enrollment = get_object_or_404(Enrollment, trainee_contract__trainee__user=request.user, course=course)
          serialized_data = TraineeCourseDashboardSerializer(data={"enrollment": enrollment})
          serialized_data.is_valid(raise_exception=True)
          return Response(serialized_data.data, status=status.HTTP_200_OK)