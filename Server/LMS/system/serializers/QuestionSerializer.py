from rest_framework import serializers
# models
from system.models.Question import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id","question","feedback","mark"]