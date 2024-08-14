from rest_framework import serializers
# models
from system.models.Content import Content
# serializers 

class ContentSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Content
        fields = ['id', 'title', 'order',"type"]
        extra_kwargs = {
            "type":{
                "read_only":True
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
    
 