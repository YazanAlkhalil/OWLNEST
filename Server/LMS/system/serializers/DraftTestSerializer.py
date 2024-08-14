from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftTest import DraftTest

#serializers 
from system.serializers.DraftQuestionSerializer import DraftQuestionSerializer
class DraftTestSerializer(ModelSerializer): 
      questions = DraftQuestionSerializer(source = "draftquestion_set",many = True,read_only = True)
      class Meta:
            model = DraftTest
            fields = ["id","questions"]
           