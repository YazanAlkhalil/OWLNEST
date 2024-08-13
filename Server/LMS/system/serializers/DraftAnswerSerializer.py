from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftAnswer import DraftAnswer
 
class DraftAnswerSerializer(ModelSerializer): 
      
      class Meta:
            model = DraftAnswer
            fields = ["id","answer","is_correct"]
           