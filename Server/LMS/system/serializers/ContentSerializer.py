from rest_framework import serializers
# models
from system.models.Content import Content
# serializers 

class ContentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Content
        fields = ['id', 'title', 'order']