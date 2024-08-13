from rest_framework import serializers
# models
from system.models.Video import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'