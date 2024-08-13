from rest_framework import serializers
# models
from system.models.Test import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id']