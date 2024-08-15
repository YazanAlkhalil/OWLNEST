from rest_framework import serializers
# models
from system.models.Question import Question
#serializers 
from system.serializers.AnswerSerializer import AnswerSerializer
from system.serializers.AnswerSerializer import TraineeAnswerSerializer

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source = 'answer_set',many = True,read_only = True)
    class Meta:
        model = Question
        fields = ["id","question","feedback","mark","answers"]


class TraineeQuestionSerializer(serializers.ModelSerializer):
    answers = TraineeAnswerSerializer(source = 'answer_set',many = True,read_only = True)
    class Meta:
        model = Question
        fields = ["id","question","feedback","mark","answers"]