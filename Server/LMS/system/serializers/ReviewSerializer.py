from rest_framework import serializers

#models 
from system.models.Review import Review
from system.models.Course import Course

class ReviewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'image']

class ReviewSerializer(serializers.ModelSerializer):
    course = ReviewCourseSerializer(read_only=True)
    trainee = serializers.CharField(source='enrollment.trainee_contract.trainee.user.username',read_only = True)
    class Meta:
        model = Review
        fields = ['id', 'description', 'rate', 'course', 'trainee']