from rest_framework import serializers
# models
from system.models.Content import Content
# serializers
from system.serializers.Pdf import Pdf_Serializer
from system.serializers.Video import Video_Serializer
from system.serializers.Test import Test_Serializer

class Content_Serializer(serializers.ModelSerializer):
    pdf = Pdf_Serializer(read_only=True)
    video = Video_Serializer(read_only=True)
    test = Test_Serializer(read_only=True)
    class Meta:
        model = Content
        fields = ['id', 'title', 'order', 'published', 'is_video', 'is_pdf', 'is_test', 'pdf', 'video', 'test']