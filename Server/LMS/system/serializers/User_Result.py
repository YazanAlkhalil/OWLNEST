from rest_framework import serializers

class User_Result_Serializer(serializers.Serializer):
    user = serializers.CharField()
    is_participant = serializers.BooleanField()