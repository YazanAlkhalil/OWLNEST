# rest_framework
from rest_framework import serializers
# models
from ..models.Trainer_Contract import Trainer_Contract
from ..models.Trainer import Trainer
from authentication.models.User import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Trainer
        fields = '__all__'

class Trainer_Contract_Serializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Trainer_Contract
        fields = ['id', 'trainer', 'company', 'joining_date']