#DRF
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
 

# models
from system.models.Favorite import Favorite 

class FavoriteSerializer(serializers.ModelSerializer): 
      class Meta:
            model = Favorite
            fields = "__all__"
     
     
      
      def to_representation(self, instance):
            data = super().to_representation(instance)
            request = self.context.get('request') 
            if instance.enrollment.course.image and request:
                data['image'] = request.build_absolute_uri(instance.enrollment.course.image.url)
            else:
                 data['image'] = None
            data["course"] = instance.enrollment.course.name
            data["course_id"] = instance.enrollment.course.id
            data["progress"]= instance.enrollment.progress
            data["rate"] = instance.enrollment.course.rate
            return data
    
      
      def to_internal_value(self, data):   
            if Favorite.objects.filter(trainee_contract=data['trainee_contract'], enrollment=data['enrollment']).exists():
              raise ValidationError({"message": "The course is already in favorites"})
            return super().to_internal_value(data)