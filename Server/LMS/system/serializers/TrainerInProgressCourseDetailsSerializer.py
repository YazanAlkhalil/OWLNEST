#DRF
from rest_framework import serializers

#models 
from system.models.Course import Course


#serializers
from system.serializers.DraftUnitSerializer import DraftUnitSerializer


class TrainerInProgressCourseDetailsSerializer(serializers.ModelSerializer):
      units = DraftUnitSerializer(source = "draft_units",many =True)
      class Meta:
            model = Course
            fields = ["id","name","image","pref_description","units"]

      