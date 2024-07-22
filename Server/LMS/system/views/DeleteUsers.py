from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from authentication.serializers.userSerializer import UserSerializer
from system.serializers.AddUserSerializer import AdminSerializer,AdminContractSerializer,TrainerSerializer,TrainerContractSerializer,TraineeSerializer,TraineeContractSerializer
from authentication.models import User
from system.models.Company import Company
from system.models.Owner import Owner
from system.serializers.Company import OwnerSerializer
from system.models.Company import Company
from system.serializers.Company import CompanySerializer
from system.models.Admin import Admin
from system.models.Trainer import Trainer
from system.models.Trainee import Trainee
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Admin_Contract import Admin_Contract
import re

from django.core.mail import send_mail
from django.conf import settings


class DeleteUser(APIView):
    def post(self, request, user_id):
        if request.user.is_authenticated:
            user = request.user
            if user is None:
                return Response({'message': 'user not found1'}, status=404)
            
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company = Company.objects.get(owner = owner)
                if User.objects.filter(id=user_id).exists():
                    emploee = User.objects.get(id= user_id)
                    if Admin.objects.filter(user_id = emploee.id).exists():
                        admin = Admin.objects.get(user_id=emploee.id)
                        if Admin_Contract.objects.filter(admin=admin,company=company.id).exists():
                            contract = Admin_Contract.objects.get(admin=admin,company=company.id)
                            contract.employed=False
                            contract.save()
                        
                    if Trainer.objects.filter(user_id = emploee.id).exists():
                        trainer = Trainer.objects.get(user_id = emploee.id)
                        if Trainer_Contract.objects.filter(trainer=trainer,company=company.id).exists():
                            contract = Trainer_Contract.objects.get(trainer=trainer,company=company.id)
                            contract.employed=False
                            contract.save()
                    
                    if Trainee.objects.filter(user_id = emploee.id).exists():
                        trainee = Trainee.objects.get(user_id = emploee.id)
                        if Trainee_Contract.objects.filter(trainee=trainee,company=company.id).exists():
                            contract = Trainee_Contract.objects.get(trainee=trainee,company=company.id)
                            contract.employed=False
                            contract.save()
                    
                    
                    return Response({'message': 'user deleted successfully'}, status=200)
                
                return Response({'message':'user nout found2'}, status=403)
            
            return Response({'message':'you are not authorized to do this action'} , status=403)
        
        return Response({'message':'user nout found3'}, status=403)



class DeleteAdmin(APIView):
    def post(self, request, user_id):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company = Company.objects.get(owner = owner)
                if User.objects.filter(id=user_id).exists():
                    emploee = User.objects.get(id= user_id)
                    if Admin.objects.filter(user_id = emploee.id).exists():
                        admin = Admin.objects.get(user_id=emploee.id)
                        if Admin_Contract.objects.filter(admin=admin,company=company.id).exists():
                            contract = Admin_Contract.objects.get(admin=admin,company=company.id)
                            contract.employed=False
                            contract.save()

                            return Response({'message':'admin deleted successfuly'} ,status = 200)
                    
                        return Response({'message':'admin nout found' }, status=403)
                    
                    return Response({'message':'admin nout found' }, status=403)
                
                return Response({'message':'user nout found' }, status=403)
            
            return Response({'message':'you are not authorized to do this action'} , status=403)
        
        return Response({'message':'user nout found' }, status=403)