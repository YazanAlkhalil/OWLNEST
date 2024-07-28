from rest_framework import serializers
# models
from ..models.Temp_unit import Temp_Unit
from ..models.Course import Course
from ..models.Unit import Unit
# serailizers
from ..serializers.Temp_Content import Temp_Content_Serializer

class Temp_Unit_Serializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False, write_only=True)
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all(), required=False, write_only=True)
    temp_contents = Temp_Content_Serializer(many=True, read_only=True, source='temp_content_set')
    class Meta:
        model = Temp_Unit
        fields = ['id', 'title', 'state', 'order', 'course', 'unit', 'temp_contents']
        extra_kwargs = {
            'state': {
                'read_only': True
            },
        }