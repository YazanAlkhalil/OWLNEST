from rest_framework.serializers import ModelSerializer

#models 
from system.models.Skill import Skill
 
class SkillSerializer(ModelSerializer):  
      class Meta:
            model = Skill
            fields = ["id","skill","rate"]
         