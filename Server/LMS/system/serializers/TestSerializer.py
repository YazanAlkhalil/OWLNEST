from rest_framework import serializers
# models
from system.models.Test import Test

#serializers 
from system.serializers.QuestionSerializer import QuestionSerializer
from system.serializers.QuestionSerializer import TraineeQuestionSerializer

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source = 'question_set',many = True,read_only = True)
    class Meta:
        model = Test
        fields = ['id','questions']


class TraineeTestSerializer(serializers.ModelSerializer):
    questions = TraineeQuestionSerializer(source = 'question_set',many = True,read_only = True)
    class Meta:
        model = Test
        fields = ['id','questions']