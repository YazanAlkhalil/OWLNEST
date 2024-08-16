#DRF
from rest_framework import serializers


#models 
from system.models.Course import Course 
from system.models.Trainer_Contract import Trainer_Contract


class TrainerCourseInfoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    username = serializers.CharField(source = "trainer.user.username")
    class Meta:
        model = Trainer_Contract
        fields = ["id", "username", "image_url"]

    def get_image_url(self, instance):
        request = self.context.get('request')
        if instance.trainer.user.image and request:
            return request.build_absolute_uri(instance.trainer.user.image.url)
        return None

class CourseInfoSerializer(serializers.ModelSerializer):
    trainers = TrainerCourseInfoSerializer( many=True, read_only=True ) 
    resource = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ["id", "trainers", "description", "resource"]


    def get_resource(self,obj):
        if hasattr(obj , 'resource'):
            print(obj)
            return obj.resource.text
         
        return str()