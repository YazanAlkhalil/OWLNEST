from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftAdditionalResources import DraftAdditionalResources
 
class DraftAdditionalResourcesSerializer(ModelSerializer):  
      class Meta:
            model = DraftAdditionalResources
            fields = ["id","text"]
         