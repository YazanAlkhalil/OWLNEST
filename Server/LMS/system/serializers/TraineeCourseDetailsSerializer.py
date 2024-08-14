#DRF 
from rest_framework import serializers


#models 
from system.models.Course import Course

#serializers
from system.serializers.UnitSerializer import UnitSerializer

class TraineeCourseDetailsSerializer(serializers.ModelSerializer):
      units = UnitSerializer(many = True, read_only = True)
      class Meta:
            model = Course 
            fields = ["id","units"]
