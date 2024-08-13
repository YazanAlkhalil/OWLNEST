from rest_framework import serializers
# models
from ..models.Temp_Content import Temp_Content
# serializers
from ..serializers.Pdf import PdfSerializer
from ..serializers.Video import VideoSerializer
from ..serializers.Test import TestSerializer

class Temp_Content_Serializer(serializers.ModelSerializer):
    # temp_unit = serializers.PrimaryKeyRelatedField(queryset=Temp_Unit.objects.all())
    # content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all())
    pdf = PdfSerializer(read_only=True)
    video = VideoSerializer(read_only=True)
    test = TestSerializer(read_only=True)
    class Meta:
        model = Temp_Content
        fields = ['id', 'title', 'state', 'order', 'is_video', 'is_pdf', 'is_test', 'pdf', 'video', 'test']
        extra_kwargs = {
            'state': {
                'read_only': True
            }
        }
    def create(self, validated_data):
        test_data = validated_data.pop('test_data', None)
        temp_content = Temp_Content.objects.create(**validated_data)
        if test_data is not None:
            test_serializer = TestSerializer(context={'temp_content': temp_content})
            test_serializer.create(test_data)
        return temp_content