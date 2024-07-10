from rest_framework import serializers
from system.models.Owner import Owner
from system.models.Company import Company

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','user']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','owner','name','email','logo','country','location','phone','size','description']
        