#DRF
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#serializers
from system.serializers.ReviewSerializer import ReviewSerializer
#models
from system.models.Review import Review
from system.models.Course import Course
from system.models.Enrollment import Enrollment
#django 
from django.shortcuts import get_object_or_404
from ..permissions.Trainee import IsTrainee, IsCompanyTrainee, IsCourseTrainee
# api/trainee/company/company_id/course/course_id/review
class ListCreateReviewView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsTrainee, IsCompanyTrainee, IsCourseTrainee]
    lookup_url_kwarg = 'course_id'
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        user = self.request.user
        return Review.objects.filter(course__id=course_id, enrollment__trainee_contract__trainee=user.trainee)
    def post(self, request, *args, **kwargs):
        course_id = self.kwargs['course_id']
        course = get_object_or_404(Course, id=course_id)
        enrollment = get_object_or_404(Enrollment, trainee_contract__trainee=request.user.trainee, course__id=course_id)
        data = {
            'description': request.data['description'],
            'rate': request.data['rate']
        }
        try:
            serialized_review = ReviewSerializer(data = data)
            serialized_review.is_valid(raise_exception=True)
            serialized_review.save(course=course, enrollment=enrollment)
        except Exception:
            return Response({'message': f'Trainee {request.user} Couldn\'t make more than one review'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serialized_review.data, status=status.HTTP_201_CREATED)