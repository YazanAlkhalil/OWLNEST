from rest_framework import serializers
# models
from ..models.Pdf import Pdf

class Pdf_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = '__all__'