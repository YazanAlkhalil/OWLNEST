from rest_framework import serializers
# models
from ..models.Temp_Content import Temp_Content

class Temp_Content_Serializer(serializers.ModelSerializer):
    # temp_unit = serializers.PrimaryKeyRelatedField(queryset=Temp_Unit.objects.all())
    # content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all())
    class Meta:
        model = Temp_Content
        fields = ['id', 'title', 'state', 'order', 'is_video', 'is_pdf', 'is_test']
        extra_kwargs = {
            'state': {
                'read_only': True
            }
        }