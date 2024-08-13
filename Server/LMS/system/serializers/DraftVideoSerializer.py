from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftVideo import DraftVideo
 
class DraftVideoSerializer(ModelSerializer): 
      class Meta:
            model = DraftVideo
            fields = ["id","file","description"]
            extra_kwargs = {
                  "file":{
                        "write_only":True
                  }
            }