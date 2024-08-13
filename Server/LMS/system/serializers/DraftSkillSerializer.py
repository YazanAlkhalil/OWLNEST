from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftSkill import DraftSkill
 
class DraftSkillSerializer(ModelSerializer):  
      class Meta:
            model = DraftSkill
            fields = ["id","skill","rate"]
         