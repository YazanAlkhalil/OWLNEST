#DRF
from rest_framework import serializers

#models 
from system.models.Finished_Content import Finished_Content
from system.models.Finished_Unit import Finished_Unit

class MarkContentSerializer(serializers.ModelSerializer):
      class Meta:
            model = Finished_Content
            fields = ['content','enrollment']
 