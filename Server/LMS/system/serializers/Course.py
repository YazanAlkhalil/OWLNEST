from rest_framework import serializers
# models
from ..models.Course import Course
from ..models.Additional_Resources import Additional_Resources
from ..models.Trainer_Contract import Trainer_Contract
from ..models.Company import Company
from authentication.models.User import User
from ..models.Admin import Admin
from ..models.Admin_Contract import Admin_Contract
from ..models.Trainer import Trainer
from ..models.Trainer_Contract import Trainer_Contract
from ..models.Trainer_Contract_Course import Trainer_Contract_Course
# serializers
from ..serializers.Additional_resources import Additional_Resources_Serializer
from ..serializers.Unit import Unit_Serializer

class CompanyNameLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'logo']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Admin
        fields = '__all__'

class AdminContractSerializer(serializers.ModelSerializer):
    admin = AdminSerializer(read_only=True)
    class Meta:
        model = Admin_Contract
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Trainer
        fields = '__all__'

class TrainerContractSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    class Meta:
        model = Trainer_Contract
        fields = ['id', 'trainer']

class TrainerContractCourseSerializer(serializers.ModelSerializer):
    trainer_contract = TrainerContractSerializer(read_only=True)
    class Meta:
        model = Trainer_Contract_Course
        fields = ['id', 'trainer_contract']

class Course_Serializer(serializers.ModelSerializer):
    additional_resources = Additional_Resources_Serializer(many=True, required=False)
    # trainers = serializers.PrimaryKeyRelatedField(queryset=Trainer_Contract.objects.all(), many=True, required=False)
    units = Unit_Serializer(many=True, read_only=True, source='unit_set')
    company = CompanyNameLogoSerializer(read_only=True)
    admin_contract = AdminContractSerializer(read_only=True)
    trainers = TrainerContractCourseSerializer(source='trainer_contract_course_set', many=True, read_only=True)
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Course
        fields = ['id', 'company', 'admin_contract', 'name', 'image', 'pref_description', 'description', 'additional_resources', 'trainers', 'units']
        extra_kwargs = {
            'company': {
                'required': False
            },
            'admin_contract': {
                'required': False
            }
        }
    # when the view_type is list send only the specified fields not all of them
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
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
                'trainers': representation['trainers'],
                'units': representation['units']
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
    def update(self, instance, validated_data):
        if 'additional_resources' in validated_data:
            additional_resources_data = validated_data.pop('additional_resources', [])
            instance = super().update(instance, validated_data)
            for additional_resource in additional_resources_data:
                resource = Additional_Resources.objects.get_or_create(**additional_resource)
                instance.additional_resources = resource
            return instance
        else:
            instance = super().update(instance, validated_data)
        return instance