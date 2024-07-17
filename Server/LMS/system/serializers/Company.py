from rest_framework import serializers
from system.models.Owner import Owner
from system.models.Company import Company
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from PIL import Image

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','user']


class CompanySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email])

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError(_('Email must be a Gmail address'))
        return value
    
    

    class Meta:
        model = Company
        fields = ['id','owner','name','email','logo','country','location','phone','size','description']