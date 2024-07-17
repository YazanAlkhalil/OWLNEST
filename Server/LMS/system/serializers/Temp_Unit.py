from rest_framework import serializers
# models
from ..models.Temp_unit import Temp_Unit
from ..models.Course import Course
from ..models.Unit import Unit

class Temp_Unit_Serializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False, write_only=True)
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all(), required=False, write_only=True)
    class Meta:
        model = Temp_Unit
        fields = '__all__'
        extra_kwargs = {
            'state': {
                'read_only': True
            },
        }