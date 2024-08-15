from rest_framework import serializers
# models
from system.models.Answer import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id","answer","is_correct"]

class TraineeAnswerSerializer(AnswerSerializer):
      class Meta(AnswerSerializer.Meta):
            fields = ["id","answer"]
           