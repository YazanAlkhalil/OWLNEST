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


class EditCompanyView(APIView):
    def post(self,request):
        if request.user.is_authenticated:
            id = request.user.id
            User = request.user
            if User is None:
                return Response({'message': 'user not found'}, status=404)
            company = Company.objects.get(id=id)

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
            
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company_qs = Company.objects.filter(owner=owner)
                for company in company_qs:
                    companies.append({
                        'id': company.id,
                        'name': company.name,
                        'logo': company.logo.url
                    })

            if Admin.objects.filter(user=user).exists():
                admin = Admin.objects.get(user=user)
                contract_qs = Admin_Contract.objects.filter(admin=admin)
                for contract in contract_qs:
                    company = Company.objects.get(id=contract.company.id)
                    companies.append({
                        'id': company.id,
                        'name': company.name,
                        'logo': company.logo.url
                    })

            if Trainer.objects.filter(user=user).exists():
                trainer = Trainer.objects.get(user=user)
                contract_qs = Trainer_Contract.objects.filter(trainer=trainer)
                for contract in contract_qs:
                    company = Company.objects.get(id=contract.company.id)
                    companies.append({
                        'id': company.id,
                        'name': company.name,
                        'logo': company.logo.url
                    })

            if Trainee.objects.filter(user=user).exists():
                trainee = Trainee.objects.get(user=user)
                contract_qs = Trainee_Contract.objects.filter(trainee=trainee)
                for contract in contract_qs:
                    company = Company.objects.get(id=contract.company.id)
                    companies.append({
                        'id': company.id,
                        'name': company.name,
                        'logo': company.logo.url
                    })


            return Response(companies, status=status.HTTP_200_OK)
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

