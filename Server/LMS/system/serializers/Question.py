from rest_framework import serializers
# models
from ..models.Question import Question
from ..models.Answer import Answer
# serialzers
from ..serializers.Answer import AnswerSerializer

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, source='answer_set')
    class Meta:
        model = Question
        fields = ['question', 'feedback', 'mark', 'answers']
        extra_kwargs = {
            'mark': {
                'required': True
            }
        }
    # custom creation
    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question