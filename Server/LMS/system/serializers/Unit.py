from rest_framework import serializers
from ..models.Unit import Unit
# serializers
from ..serializers.Content import Content_Serializer

class Unit_Serializer(serializers.ModelSerializer):
    contents = Content_Serializer(many=True, read_only=True, source='content_set')
    class Meta:
        model = Unit
        fields = ['id', 'title', 'order', 'contents']