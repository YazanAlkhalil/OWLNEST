from rest_framework import serializers
from authentication.models.User import User
from system.models.Admin import Admin
from system.models.Admin_Contract import Admin_Contract
from system.models.Trainer import Trainer
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainee import Trainee
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Company import Company


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id','user']

class AdminContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Contract
        fields = ['id','admin','company']



class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id','user']

class TrainerContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer_Contract
        fields = ['id','trainer','company']



class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id','user']

class TraineeContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee_Contract
        fields = ['id','trainee','company']

