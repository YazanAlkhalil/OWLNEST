from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftUnit import DraftUnit

#serializers 
from system.serializers.DraftContentSerializer import DraftContentserializer
class DraftUnitSerializer(ModelSerializer):
      contents = DraftContentserializer(many = True,read_only = True)
      class Meta:
            model = DraftUnit
            fields = ["id","title","order","contents"]
            extra_kwargs = {
                  "order":{
                        "write_only":True
                  }
            }