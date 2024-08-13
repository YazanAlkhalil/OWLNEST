from rest_framework.serializers import ModelSerializer

#models 
from system.models.DraftPDF import DraftPDF

#serializers 
from system.serializers.DraftContentSerializer import DraftContentserializer

class DraftPDFSerializer(ModelSerializer): 
      class Meta:
            model = DraftPDF
            fields = ["id","file"]
            extra_kwargs = {
                  "file":{
                        "write_only":True
                  }
            }