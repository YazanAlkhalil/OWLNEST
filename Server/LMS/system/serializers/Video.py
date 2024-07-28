from rest_framework import serializers
# models
from ..models.Video import Video

class Video_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'