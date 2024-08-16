#DRF 
from rest_framework import serializers

#models 
from system.models.Review import Review
from system.models.Course import Course
from system.models.Enrollment import Enrollment
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Trainee import Trainee
from authentication.models.User import User

class ReviewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'image']

class UserCourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TraineeCourseReviewSerializer(serializers.ModelSerializer):
    user = UserCourseReviewSerializer(read_only=True)
    class Meta:
        model = Trainee
        fields = ['user']

class TraineeContractCourseReviewSerializer(serializers.ModelSerializer):
    trainee = TraineeCourseReviewSerializer(read_only=True)
    class Meta:
        model = Trainee_Contract
        fields = ['trainee']

class EnrollmentCourseReviewSerializer(serializers.ModelSerializer):
    trainee_contract = TraineeContractCourseReviewSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = ['trainee_contract']

class ReviewSerializer(serializers.ModelSerializer):
    course = ReviewCourseSerializer(read_only=True)
    trainee = EnrollmentCourseReviewSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'description', 'rate', 'course', 'trainee']