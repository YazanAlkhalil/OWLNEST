from rest_framework import serializers
# models
from ..models.Temp_Content import Temp_Content
from ..models.Temp_unit import Temp_Unit
from ..models.Content import Content

class Temp_Content_Serializer(serializers.ModelSerializer):
    temp_unit = serializers.PrimaryKeyRelatedField(queryset=Temp_Unit.objects.all())
    content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all())
    class Meta:
        model = Temp_Content
        fields = '__all__'
        extra_kwargs = {
            'state': {
                'read_only': True
            }
        }