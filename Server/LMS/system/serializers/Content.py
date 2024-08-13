from rest_framework import serializers
# models
from ..models.Content import Content
# serializers
from ..serializers.Pdf import PdfSerializer
from ..serializers.Video import VideoSerializer
from ..serializers.Test import TestSerializer

class Content_Serializer(serializers.ModelSerializer):
    pdf = PdfSerializer(read_only=True)
    video = VideoSerializer(read_only=True)
    test = TestSerializer(read_only=True)
    class Meta:
        model = Content
        fields = ['id', 'title', 'order', 'published', 'is_video', 'is_pdf', 'is_test', 'pdf', 'video', 'test']