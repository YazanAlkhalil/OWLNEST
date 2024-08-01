#DRF
from rest_framework import serializers

#models 
from system.models.Course import Course




class TrainerCourseListSerializer(serializers.ModelSerializer):
      class Meta:
            model = Course
            fields = ["id","name","image"]

      