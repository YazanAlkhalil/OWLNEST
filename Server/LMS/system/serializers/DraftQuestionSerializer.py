from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftQuestion import DraftQuestion

#serializers 
from system.serializers.DraftAnswerSerializer import DraftAnswerSerializer

class DraftQuestionSerializer(ModelSerializer): 
      answers = DraftAnswerSerializer(source = "draftanswer_set",many = True,read_only = True)
      class Meta:
            model = DraftQuestion
            fields = ["id","question","feedback","answers","mark"]
           