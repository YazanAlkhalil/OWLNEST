from rest_framework import serializers
# models
from ..models.Unit import Unit

class Unit_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'