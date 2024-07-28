# rest_framework
from rest_framework import serializers
# models
from ..models.Trainer_Contract import Trainer_Contract
# serializer
from .Course import TrainerSerializer

class Trainer_Contract_Serializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Trainer_Contract
        fields = ['id', 'trainer', 'company', 'joining_date']