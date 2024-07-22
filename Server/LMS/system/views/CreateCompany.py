from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.serializers.userSerializer import UserSerializer
from authentication.models import User

from system.models.Owner import Owner
from system.serializers.Company import OwnerSerializer
from system.models.Company import Company
from system.serializers.Company import CompanySerializer
from system.models.Wallet import Wallet
from system.serializers.Wallet import WalletSerializer
from system.models.Admin import Admin
from system.models.Trainer import Trainer
from system.models.Trainee import Trainee
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Admin_Contract import Admin_Contract
from rest_framework.exceptions import AuthenticationFailed


class CreateCompanyView(APIView):
    def post(self,request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)

            owner_data = {
                'user': user
                }
            owner = Owner.objects.create(**owner_data)
            data = request.data
            wallet_data = {
                'owner':owner
            }
            wallet = Wallet.objects.create(**wallet_data)
            
            company_data = request.data
            company_data.pop('user', None) 
            company_data['owner'] = owner.id
            
            serializer = CompanySerializer(data = company_data)

            if serializer.is_valid(): 
                serializer.save()

                user.is_owner = True
                user.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                owner.delete()
                wallet.delete()
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'user not found'}, status=401)

class CompanyView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if User is None:
                return Response({'message': 'user not found'}, status=404)
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company = Company.objects.get(owner=owner)
                return Response(CompanySerializer(company).data)
        raise AuthenticationFailed('unauthenticated')

class EditCompanyView(APIView):
    def patch(self,request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if User is None:
                return Response({'message': 'user not found'}, status=404)
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company = Company.objects.get(owner=owner)
                company_data = request.data
                serializer = CompanySerializer(company, data=company_data, partial=True)
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'user is not an owner'}, status=403)
        return Response({'message': 'user not found'}, status=401)

class DeleteOwnerView(APIView):
    def delete(self, request):
        pk = request.data['id']
        owner = Owner.objects.filter(pk=pk).first()
        if owner:
            owner.delete()
            return Response({'message': 'owner deleted successfully'})
        else:
            return Response({'message': 'owner not found'}, status=404)
        

class CompaniesView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            
            companies = []
            company_ids = set() 
            
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company_qs = Company.objects.filter(owner=owner)
                for company in company_qs:
                    if company.id not in company_ids:
                        companies.append({
                            'id': company.id,
                            'name': company.name,
                            'logo': company.logo.url,
                            'owner':True
                        })
                        company_ids.add(company.id)

            if Admin.objects.filter(user=user).exists():
                admin = Admin.objects.get(user=user)
                contract_qs = Admin_Contract.objects.filter(admin=admin)
                con = Admin_Contract.objects.get(admin=admin)
                if con.employed is True:
                    for contract in contract_qs:
                        company = Company.objects.get(id=contract.company.id)
                        if company.id not in company_ids:
                            companies.append({
                                'id': company.id,
                                'name': company.name,
                                'logo': company.logo.url
                            })
                            company_ids.add(company.id)

            if Trainer.objects.filter(user=user).exists():
                trainer = Trainer.objects.get(user=user)
                contract_qs = Trainer_Contract.objects.filter(trainer=trainer)
                con = Trainer_Contract.objects.get(trainer=trainer)
                if con.employed is True:
                    for contract in contract_qs:
                        company = Company.objects.get(id=contract.company.id)
                        if company.id not in company_ids:
                            companies.append({
                                'id': company.id,
                                'name': company.name,
                                'logo': company.logo.url
                            })
                            company_ids.add(company.id)

            if Trainee.objects.filter(user=user).exists():
                trainee = Trainee.objects.get(user=user)
                contract_qs = Trainee_Contract.objects.filter(trainee=trainee)
                con = Trainee_Contract.objects.get(trainee=trainee)
                if con.employed is True:
                    for contract in contract_qs:
                        company = Company.objects.get(id=contract.company.id)
                        if company.id not in company_ids:
                            companies.append({
                                'id': company.id,
                                'name': company.name,
                                'logo': company.logo.url
                            })
                            company_ids.add(company.id)
            
            response = Response()
            response.data = {
                'username': user.username,
                'companies':companies,
            }

            return response
        return Response({'message': 'user not found'}, status=401)


class CompanyUsers(APIView):
    def get(self, request,company_id):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            
            if not Company.objects.filter(id=company_id).exists():
                return Response({'message': 'company not found'}, status=404)
            company = Company.objects.get(id=company_id)

            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                if Company.objects.filter(owner=owner,id=company.id).exists():
                    # company = Company.objects.get(owner=owner,id=company.id)
                    users = {}
                    for admin_contract in Admin_Contract.objects.filter(company=company):
                        if admin_contract.employed is True:
                            admin = admin_contract.admin
                            user_id = admin.user.id
                            if user_id not in users:
                                users[user_id] = {
                                    'id': admin.user.id,
                                    'username': admin.user.username,
                                    'roles': [],
                                    'last_login':admin.user.last_login
                                }
                            users[user_id]['roles'].append('admin')
                    for trainer_contract in Trainer_Contract.objects.filter(company=company):
                        if trainer_contract.employed is True:
                            trainer = trainer_contract.trainer
                            user_id = trainer.user.id
                            if user_id not in users:
                                users[user_id] = {
                                    'id': trainer.user.id,
                                    'username': trainer.user.username,
                                    'roles': [],
                                    'last_login':trainer.user.last_login
                                }
                            users[user_id]['roles'].append('trainer')
                    for trainee_contract in Trainee_Contract.objects.filter(company=company):
                        if trainee_contract.employed is True:
                            trainee = trainee_contract.trainee
                            user_id = trainee.user.id
                            if user_id not in users:
                                users[user_id] = {
                                    'id': trainee.user.id,
                                    'username': trainee.user.username,
                                    'roles': [],
                                    'last_login':trainee.user.last_login
                                }
                            users[user_id]['roles'].append('trainee')
                    return Response(list(users.values()))
            elif Admin.objects.filter(user=user).exists():
                admin = Admin.objects.get(user=user)
                if Admin_Contract.objects.filter(admin=admin,company=company).exists():
                    # company =Company.objects.get(company=company)
                    users = {}
                    for admin_contract in Admin_Contract.objects.filter(company=company):
                        if admin_contract.employed is True:
                            admin = admin_contract.admin
                            user_id = admin.user.id
                            if user_id not in users:
                                users[user_id] = {
                                    'id': admin.user.id,
                                    'username': admin.user.username,
                                    'roles': [],
                                    'last_login':admin.user.last_login
                                }
                            users[user_id]['roles'].append('admin')
                    for trainer_contract in Trainer_Contract.objects.filter(company=company):
                        if trainer_contract.employed is True:
                            trainer = trainer_contract.trainer
                            user_id = trainer.user.id
                            if user_id not in users:
                                users[user_id] = {
                                    'id': trainer.user.id,
                                    'username': trainer.user.username,
                                    'roles': [],
                                    'last_login':trainer.user.last_login
                                }
                            users[user_id]['roles'].append('trainer')
                    for trainee_contract in Trainee_Contract.objects.filter(company=company):
                        if trainee_contract.employed is True:
                            trainee = trainee_contract.trainee
                            user_id = trainee.user.id
                            if user_id not in users:
                                users[user_id] = {
                                    'id': trainee.user.id,
                                    'username': trainee.user.username,
                                    'roles': [],
                                    'last_login':trainee.user.last_login
                                }
                            users[user_id]['roles'].append('trainee')
                    return Response(list(users.values()))
                else:
                    return Response({'message':'You are not authorized to access this page.'})
                
            else:
                return Response({'message': 'You are not authorized to access this page'}, status=403)
        return Response({'message': 'user not found'}, status=401)


class DeleteCompanyView(APIView):
    def delete(self, request):
        pk = request.data['id']
        company = Company.objects.filter(pk=pk).first()
        if company:
            company.delete()
            return Response({'message': 'company deleted successfully'})
        else:
            return Response({'message': 'company not found'}, status=404)


class UserCompanyView(APIView):
    def get(self, request,company_id):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            if not Company.objects.filter(id=company_id).exists():
                return Response({'message': 'company not found'}, status=404)
        
            company = Company.objects.get(id=company_id)
            roles = []
            
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                if Company.objects.filter(owner=owner, id=company.id).exists():
                    roles.append('owner')

            if Admin.objects.filter(user=user).exists():
                admin = Admin.objects.get(user=user)
                if Admin_Contract.objects.filter(admin=admin, company=company).exists():
                    con = Admin_Contract.objects.get(admin=admin,company=company)
                    if con.employed is True:
                        roles.append('admin')
            
            if Trainer.objects.filter(user=user).exists():
                trainer = Trainer.objects.get(user=user)
                if Trainer_Contract.objects.filter(trainer=trainer,company=company).exists():
                    con = Trainer_Contract.objects.get(trainer=trainer,company=company)
                    if con.employed is True:
                        roles.append('trainer')

            if Trainee.objects.filter(user=user).exists():
                trainee = Trainee.objects.get(user=user)
                if Trainee_Contract.objects.filter(trainee=trainee,company=company).exists():
                    con = Trainee_Contract.objects.get(trainee=trainee,company=company)
                    if con.employed is True:
                        roles.append('trainee')
            
            return  Response(roles , status =200)
        
        return Response({'message': 'user not found'}, status=401)


