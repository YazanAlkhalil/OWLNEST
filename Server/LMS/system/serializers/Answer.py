from rest_framework import serializers
# models
from ..models.Answer import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct']
        extra_kwargs = {
            'is_correct': {
                'required': True
            }
        }