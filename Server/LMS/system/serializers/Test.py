from rest_framework import serializers
# models
from ..models.Test import Test

class Test_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'