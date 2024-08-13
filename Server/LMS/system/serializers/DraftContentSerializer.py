from rest_framework import serializers

#models 
from system.models.DraftContent import DraftContent

class DraftContentserializer(serializers.ModelSerializer):
      type = serializers.SerializerMethodField()
      class Meta:
            model = DraftContent
            fields = ["id","title","order","type"]
            extra_kwargs = {
                  "order":{
                        "write_only":True
                  }
            }

      def get_type(self, obj):
        if obj.is_video:
            return "video"
        elif obj.is_pdf:
            return "pdf"
        elif obj.is_test:
            return "test"
        return None