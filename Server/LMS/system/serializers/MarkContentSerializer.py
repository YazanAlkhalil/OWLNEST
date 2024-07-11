#DRF
from rest_framework import serializers

#models 
from system.models.Finished_Content import Finished_Content
from system.models.Finished_Unit import Finished_Unit

class MarkContentSerializer(serializers.ModelSerializer):
      class Meta:
            model = Finished_Content
            fields = ['content']
 
      def to_internal_value(self, data):
            enrollment = data["enrollment"]
            xp = data["xp"]
            data =  super().to_internal_value(data)
            data["enrollment"] = enrollment
            data["xp"] = xp
            return data
      def create(self, validated_data): 
            return super().create(validated_data)