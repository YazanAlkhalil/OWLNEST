from rest_framework import serializers
# models
from ..models.Pdf import Pdf

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = '__all__'