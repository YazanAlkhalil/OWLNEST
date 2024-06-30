from rest_framework import serializers
from ..models.Trainer_Contract_Course import Trainer_Contract_Course

class Trainer_Contract_Course_Serializer(serializers.ModelSerializer):
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Trainer_Contract_Course
        fields = ['id', 'course', 'trainer_contract', 'start_date']