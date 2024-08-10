# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Sum, Count
from system.models.Enrollment import Enrollment 

from system.models.Course import Course 
from system.serializers.TraineeInCourseSerializer import TraineesInCourseSerializer

class TraineesInCoursView(APIView):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id)
        enrollments = Enrollment.objects.filter(
            course=course,
            trainee_contract__employed=True
        ).annotate(
            avg_grade=Avg('grade__score'),
            total_xp=Sum('grade__xp') + (Count('finished_content') * 10)
        ).select_related('trainee_contract__trainee__user')

        serializer = TraineesInCourseSerializer(enrollments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
