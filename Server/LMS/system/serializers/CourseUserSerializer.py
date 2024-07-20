from rest_framework import serializers
from authentication.models.User import User



class UserSerializer(serializers.ModelSerializer):
    is_participant = serializers.BooleanField()
    role = serializers.CharField()
    completed_at = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'is_participant', 'role', 'completed_at', 'id']