from rest_framework import serializers
# models
from ..models.Test import Test
from ..models.Question import Question
from ..models.Answer import Answer
# serialzier
from ..serializers.Question import QuestionSerializer
class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')
    class Meta:
        model = Test
        fields = ['content', 'temp_content', 'full_mark', 'questions']
        extra_kwargs = {
            'full_mark': {
                'required': False,
                "default": 0.0
            },
            'content': {
                'write_only': True
            },
            'temp_content': {
                'write_only': True
            }
        }
    # custom creation
    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        test = Test.objects.create(**validated_data)
        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(test=test, **question_data)
            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)
        return test