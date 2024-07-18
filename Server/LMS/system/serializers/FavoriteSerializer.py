#DRF
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
 

# models
from system.models.Favorite import Favorite 

class FavoriteSerializer(serializers.ModelSerializer):

      class Meta:
            model = Favorite
            fields = '__all__'


      def to_representation(self, instance):
            data = dict() 
            data["course"] = instance.enrollment.course.name
            data["image"] = instance.enrollment.course.image.url if instance.enrollment.course.image else None
            data["progress"]= instance.enrollment.progress
            data["trainer"] = "mutaz"
            return data
      
      def to_internal_value(self, data):   
            if Favorite.objects.filter(trainee_contract=data['trainee_contract'], enrollment=data['enrollment']).exists():
              raise ValidationError({"message": "The course is already in favorites"})
            return super().to_internal_value(data)