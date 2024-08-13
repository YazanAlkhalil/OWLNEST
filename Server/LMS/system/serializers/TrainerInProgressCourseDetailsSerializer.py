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


      def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request') 
        if instance.image and request:
            representation['image'] = request.build_absolute_uri(instance.image.url)
        return representation