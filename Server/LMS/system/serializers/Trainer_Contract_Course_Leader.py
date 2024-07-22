# rest_framework
from rest_framework import serializers
# models
from ..models.Trainer_Contract_Course import Trainer_Contract_Course
# serializers
from ..serializers.Course import Course_Serializer
from ..serializers.Trainer_Contract import Trainer_Contract_Serializer

class Trainer_Contract_Course_Leader_Serializer(serializers.ModelSerializer):
    # course = Course_Serializer(read_only=True, required=False)
    trainer_contract = Trainer_Contract_Serializer(read_only=True)
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Trainer_Contract_Course
        fields = ['id', 'is_leader', 'trainer_contract', 'start_date']