from rest_framework import serializers
from ..models.Trainer_Contract import Trainer_Contract

class Trainer_Contract_Serializer(serializers.ModelSerializer):
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Trainer_Contract
        fields = ['id', 'trainer', 'company', 'joining_date']