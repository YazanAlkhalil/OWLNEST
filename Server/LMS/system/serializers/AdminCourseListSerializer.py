#DRF
from rest_framework import serializers

#models 
from system.models.Course import Course




class AdminCourseListSerializer(serializers.ModelSerializer):
      class Meta:
            model = Course
            fields = ["id","name","image"]

      