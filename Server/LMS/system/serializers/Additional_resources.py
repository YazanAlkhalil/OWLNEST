from rest_framework import serializers
from ..models.Additional_Resources import Additional_Resources

class Additional_Resources_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_Resources
        fields = ['id', 'resource_link']