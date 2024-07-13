from rest_framework import serializers
# models
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit

class Unit_Serializer(serializers.ModelSerializer):
    temp_unit = serializers.PrimaryKeyRelatedField(queryset=Temp_Unit.objects.all())
    class Meta:
        model = Unit
        fields = '__all__'