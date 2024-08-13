from rest_framework.serializers import ModelSerializer

#models 
from system.models.Additional_Resources import Additional_Resources
 
class AdditionalResourceSerializer(ModelSerializer):  
      class Meta:
            model = Additional_Resources
            fields = ["id","text"]
         