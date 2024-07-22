from rest_framework import serializers
# models
from authentication.models.User import User
from ..models.Admin import Admin
from ..models.Admin_Contract import Admin_Contract
from ..models.Trainer import Trainer
from ..models.Trainer_Contract import Trainer_Contract
from ..models.Trainer_Contract_Course import Trainer_Contract_Course
from ..models.Company import Company
from ..models.Course import Course
# serializers
from ..serializers.Temp_Unit import Temp_Unit_Serializer

class Company_Name_Logo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'logo']

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class Admin_Serializer(serializers.ModelSerializer):
    user = User_Serializer(read_only=True)
    class Meta:
        model = Admin
        fields = '__all__'

class Admin_Contract_Serializer(serializers.ModelSerializer):
    admin = Admin_Serializer(read_only=True)
    class Meta:
        model = Admin_Contract
        fields = '__all__'

class Trainer_Serializer(serializers.ModelSerializer):
    user = User_Serializer(read_only=True)
    class Meta:
        model = Trainer
        fields = '__all__'

class Trainer_Contract_Serializer(serializers.ModelSerializer):
    trainer = Trainer_Serializer(read_only=True)
    class Meta:
        model = Trainer_Contract
        fields = ['id', 'trainer']

class Trainer_Contract_Course_Serializer(serializers.ModelSerializer):
    trainer_contract = Trainer_Contract_Serializer(read_only=True)
    class Meta:
        model = Trainer_Contract_Course
        fields = ['id', 'trainer_contract']

class Course_Pending_Progress_Serializer(serializers.ModelSerializer):
    temp_units = Temp_Unit_Serializer(many=True, read_only=True, source='temp_unit_set')
    company = Company_Name_Logo_Serializer(read_only=True)
    admin_contract = Admin_Contract_Serializer(read_only=True)
    trainers = Trainer_Contract_Course_Serializer(source='trainer_contract_course_set', many=True, read_only=True)
    # sepcify the model for the serializer and the required fields
    class Meta:
        model = Course
        fields = ['id', 'company', 'admin_contract', 'name', 'image', 'pref_description', 'trainers', 'temp_units']
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
                'units': representation['temp_units']
            }