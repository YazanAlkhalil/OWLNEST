from rest_framework import serializers
# models
from ..models.Content import Content

class Content_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'order', 'is_video', 'is_pdf', 'is_test']
