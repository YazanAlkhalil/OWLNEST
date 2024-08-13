#DRF
from rest_framework import serializers

#models 
from system.models.AdminApprovment import AdminApprovment




class AdminApprovmentSerializer(serializers.ModelSerializer):
      class Meta:
            model = AdminApprovment
            fields = ["id","admin_contract","course"]

      