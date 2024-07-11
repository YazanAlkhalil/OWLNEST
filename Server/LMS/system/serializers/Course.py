from rest_framework import serializers
# models
from ..models.Course import Course
from ..models.Additional_Resources import Additional_Resources
from ..models.Trainer_Contract import Trainer_Contract
# serializers
from ..serializers.Additional_resources import Additional_Resources_Serializer

'''
    TODO:
    in the detail request type add the course units and contents
'''

class Course_Serializer(serializers.ModelSerializer):
    additional_resources = Additional_Resources_Serializer(many=True, required=False)
    trainers = serializers.PrimaryKeyRelatedField(queryset=Trainer_Contract.objects.all(), many=True)
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Course
        fields = ['id', 'company', 'admin_contract', 'name', 'image', 'pref_description', 'description', 'expected_time', 'additional_resources', 'trainers']
    # when the view_type is list send only the specified fields not all of them
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view_type') == 'list':
            return {
                'id': representation['id'],
                'name': representation['name'],
                'image': representation['image']
            }
        if self.context.get('view_type') == 'detail':
            return {
                'id': representation['id'],
                'company': representation['company'],
                'admin_contract': representation['admin_contract'],
                'name': representation['name'],
                'image': representation['image'],
                'pref_description': representation['pref_description'],
                'expected_time': representation['expected_time'],
                'trainers': representation['trainers']
            }
        return representation
    # when create a new course add the trainers for this course
    def create(self, validated_data):
        trainers_data = validated_data.pop('trainers', [])
        course = Course.objects.create(**validated_data)
        for trainer in trainers_data:
            course.trainers.add(trainer)
        return course
    # when updating the course if the additional resources where given then save it in its table then set it to the course
    def update(self, validated_data):
        if validated_data['additional_resources']:
            additional_resources_data = validated_data.pop('additional_resources', [])
            course = Course.objects.create(**validated_data)
            for additional_resource in additional_resources_data:
                resource = Additional_Resources.objects.get_or_create(**additional_resource)
                course.additional_resources = resource
            return course
        else:
            pass