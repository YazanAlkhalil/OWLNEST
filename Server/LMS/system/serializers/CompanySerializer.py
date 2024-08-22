#DRF
from rest_framework import serializers

#models 
from system.models.Company import Company 


class CompanySerializer(serializers.ModelSerializer):
      is_owner = serializers.SerializerMethodField()
      logo = serializers.SerializerMethodField()
      class Meta:
            model = Company 
            fields = ["id","name","logo","is_owner","location"]

      def get_is_owner(self,obj):
          user = self.context["request"].user 
          return obj.owner.user == user
      

      def get_logo(self,obj):
          request = self.context["request"]
          return request.build_absolute_uri(obj.logo.url)