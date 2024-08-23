#DRF
from rest_framework import serializers

#models 
from system.models.OwnerApprovments import OwnerApprovment




class OwnerApprovmentSerializer(serializers.ModelSerializer):
      class Meta:
            model = OwnerApprovment
            fields = ["id","owner","course"]

      