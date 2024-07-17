#DRF
from rest_framework import serializers


# models
from system.models.Favorite import Favorite
from system.models.Enrollment import Enrollment
from system.models.Trainee_Contract import Trainee_Contract


class FavoriteSerializer(serializers.ModelSerializer):

      class Meta:
            model = Favorite
            fields = '__all__'


      def to_representation(self, instance):
            data = dict() 
            data["course"] = instance.enrollment.course.name
            data["image"] = instance.enrollment.course.image.url
            data["progress"]= instance.enrollment.progress
            data["trainer"] = "mutaz"
            return data