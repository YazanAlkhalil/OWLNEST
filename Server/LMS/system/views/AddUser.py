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

class AddUser(APIView):
    def post(self,request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            
            data = request.data
            company_id = request.query_params.get('company_id')
            if company_id is None:
                return Response({'message': 'company_id not found'}, status=404)
            company = Company.objects.get(id=company_id)

            if Admin.objects.filter(user=user).exists():
                admin = Admin.objects.get(user=user)
                if Admin_Contract.objects.filter(admin=admin, company=company.id , employed = True ).exists():
                    user_role = 'admin'
                else:
                    user_role = "null"
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                if Company.objects.filter(id=company_id, owner=owner.id).exists():
                    user_role = 'owner'
                else:
                    user_role = "null"
            
            if user_role == "null":
                return Response(
                    {'message': 'You are not authorized to perform this action'},
                    status=401
                    )
            
            email = data.get('email')
            if email == user.email:
                return Response({'message':'you are already the owner'} , status = 403)
            role = data.get('role')
            email_pattern = r'^[^@]+@gmail\.com$'
            if not re.match(email_pattern, email):
                return Response({'message': 'Invalid email address. Only Gmail addresses are allowed.'}, status=400)

            if User.objects.filter(email=email).exists():
                new_user = User.objects.get(email=email)
                # if Admin.objects.filter(user=new_user).exists():
                #     admin = Admin.objects.get(user=new_user)
                #     if Admin_Contract.objects.filter(admin= admin ,company=company):
                #         contract = Admin_Contract.objects.get(admin=admin,company=company)
                #         if contract.employed is False:
                #             contract.employed=True
                #             contract.save()
                #             return Response({'message': 'User added successfully'}, status=201)
                #         else:
                #             return Response(
                #             {'message': 'this user is already exists'},
                #             status=status.HTTP_403_FORBIDDEN
                #         )
                # if Trainer.objects.filter(user=new_user).exists():
                #     trainer = Trainer.objects.get(user=new_user)
                #     if Trainer_Contract.objects.filter(company=company,trainer= trainer):
                #         contract = Trainer_Contract.objects.get(trainer=trainer,company=company)
                #         if contract.employed is False:
                #             contract.employed=True
                #             contract.save()
                #             return Response({'message': 'User added successfully'}, status=201)
                #         else:
                #             return Response(
                #             {'message': 'this user is already exists'},
                #             status=status.HTTP_403_FORBIDDEN
                #         )
                # if Trainee.objects.filter(user=new_user).exists():
                #     trainee = Trainee.objects.get(user=new_user)
                #     if Trainee_Contract.objects.filter(trainee= trainee ,company=company) :
                #         contract = Trainee_Contract.objects.get(trainee=trainee,company=company.id)
                #         if contract.employed is False:
                #             contract.employed=True
                #             contract.save()
                #             return Response({'message': 'User added successfully'}, status=201)
                #         else:
                #             return Response(
                #             {'message': 'this user is already exists'},
                #             status=401
                #         )
                if user_role == 'admin':
                    if role not in ['Trainer', 'Trainee']:
                        return Response(
                            {'message': 'You are not authorized to perform this action'},
                            status=401
                        )
                elif user_role == 'owner':
                    if role not in ['Admin', 'Trainer', 'Trainee']:
                        return Response(
                            {'message': 'You are not authorized to perform this action'},
                            status=401
                        )

                else :
                    return Response(
                            {'message': 'You are not authorized to perform this action'},
                            status=401
                        )
                
                if role == 'Admin':
                    user = new_user
                    admin_data = {
                        'user':user.id
                    }
                    if Admin.objects.filter(user=new_user).exists():
                        admin = Admin.objects.get(user=new_user)
                        if Admin_Contract.objects.filter(admin= admin ,company=company):
                            contract = Admin_Contract.objects.get(admin=admin,company=company)
                            if contract.employed is False:
                                contract.employed=True
                                contract.save()
                                return Response({'message': 'User added successfully'}, status=201)
                            if contract.employed is True:
                                return Response(
                                {'message': 'this user is already exists'},
                                status=status.HTTP_403_FORBIDDEN
                            )
                        admin_contract_data = {
                            'admin':admin,
                            'company':company
                        }
                        Admin_Contract.objects.create(**admin_contract_data)
                    else:
                        serializer = AdminSerializer(data = admin_data)
                        if serializer.is_valid():
                            serializer.save()
                            user.is_admin = True
                            user.save()
                            admin = serializer.instance
                            admin_contract_data = {
                                'admin':admin,
                                'company':company
                            }
                            Admin_Contract.objects.create(**admin_contract_data)
                        else :
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


                elif role == 'Trainer':
                    user = new_user
                    trainer_data = {
                        'user':user.id
                    }
                    if Trainer.objects.filter(user=new_user).exists():
                        trainer = Trainer.objects.get(user=new_user)
                        if Trainer_Contract.objects.filter(company=company,trainer= trainer):
                            contract = Trainer_Contract.objects.get(trainer=trainer,company=company)
                            if contract.employed is False:
                                contract.employed=True
                                contract.save()
                                return Response({'message': 'User added successfully'}, status=201)
                            if contract.employed is True:
                                return Response(
                                {'message': 'this user is already exists'},
                                status=status.HTTP_403_FORBIDDEN
                            )
                        trainer_contract_data = {
                            'trainer':trainer,
                            'company':company
                        }
                        Trainer_Contract.objects.create(**trainer_contract_data)
                    else :
                        serializer = TrainerSerializer(data = trainer_data)
                        if serializer.is_valid():
                            serializer.save()
                            user.is_trainer = True
                            user.save()
                            trainer = serializer.instance
                            trainer_contract_data = {
                                'trainer':trainer,
                                'company':company
                            }
                            Trainer_Contract.objects.create(**trainer_contract_data)

                        else:
                            return Response({'message':'errorororor'}, status=status.HTTP_400_BAD_REQUEST)

                elif role == 'Trainee':
                    user = new_user
                    trainee_data = {
                        'user':user.id
                    }
                    if Trainee.objects.filter(user=new_user).exists():
                        trainee = Trainee.objects.get(user=new_user)
                        if Trainee_Contract.objects.filter(trainee= trainee ,company=company) :
                            contract = Trainee_Contract.objects.get(trainee=trainee,company=company.id)
                            if contract.employed is False:
                                contract.employed=True
                                contract.save()
                                return Response({'message': 'User added successfully'}, status=201)
                            if contract.employed is True:
                                return Response(
                                {'message': 'this user is already exists'},
                                status=401
                            )
                        trainee_contract_data = {
                            'trainee':trainee,
                            'company':company
                        }
                        Trainee_Contract.objects.create(**trainee_contract_data)
                    else:
                        serializer = TraineeSerializer(data = trainee_data)
                        if serializer.is_valid():
                            serializer.save()
                            user.is_trainee = True
                            user.save()
                            trainee = serializer.instance
                            trainee_contract_data = {
                                'trainee':trainee,
                                'company':company
                            }
                            Trainee_Contract.objects.create(**trainee_contract_data)
                        else :
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return Response({'message': 'User added successfully'}, status=201)

            else:
                subject = "Join a company "
                message = f"Congratulations, you have received an invitation to join the {company.name} Hurry to create an account on our platform so that you can join this company"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                return Response({'message': 'An invitation email has been sent to the user'}, status=200)

        return Response({'message': 'You are not authenticated'}, status=401)
