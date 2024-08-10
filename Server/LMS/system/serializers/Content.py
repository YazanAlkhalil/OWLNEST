from rest_framework import serializers
# models
from ..models.Content import Content
# serializers
from ..serializers.Pdf import Pdf_Serializer
from ..serializers.Video import Video_Serializer
from ..serializers.Test import Test_Serializer

class Content_Serializer(serializers.ModelSerializer):
    pdf = Pdf_Serializer(read_only=True)
    video = Video_Serializer(read_only=True)
    test = Test_Serializer(read_only=True)
    class Meta:
        model = Content
        fields = ['id', 'title', 'order', 'published', 'is_video', 'is_pdf', 'is_test', 'pdf', 'video', 'test']