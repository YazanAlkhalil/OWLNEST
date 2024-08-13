from rest_framework import serializers

#models
from system.models.Unit import Unit 

class UnitSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Unit
        fields = ['id', 'title','order']