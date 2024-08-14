from rest_framework import serializers

#models
from system.models.Unit import Unit 

#serializers
from system.serializers.ContentSerializer import ContentSerializer

class UnitSerializer(serializers.ModelSerializer): 
    contents = ContentSerializer(source = "content_set",many = True,read_only = True)
    class Meta:
        model = Unit
        fields = ['id', 'title','order',"contents"]