from rest_framework import serializers
# models
from ..models.Temp_unit import Temp_Unit
from ..models.Course import Course

class Temp_Unit_Serializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model = Temp_Unit
        fields = '__all__'
        extra_kwargs = {
            "state": {
                "read_only": True
            }
        }