from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftVideo import DraftVideo
 
class DraftVideoSerializer(ModelSerializer): 
      class Meta:
            model = DraftVideo
            fields = ["id","file"]
            extra_kwargs = {
                  "file":{
                        "write_only":True
                  }
            }