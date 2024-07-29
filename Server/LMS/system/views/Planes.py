from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.serializers.userSerializer import UserSerializer
from authentication.models import User
import decimal
from system.models.Owner import Owner
from system.serializers.Company import OwnerSerializer
from system.models.Company import Company
from system.serializers.Company import CompanySerializer
from system.models.Wallet import Wallet
from system.serializers.Wallet import WalletSerializer
from system.models.Admin import Admin
from system.models.Planes import Planes
from system.models.Trainer import Trainer
from system.models.Trainee import Trainee
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Admin_Contract import Admin_Contract
from rest_framework.exceptions import AuthenticationFailed
from system.serializers.PlaneSerializer import PlaneSerializer,CompanyPlaneSerializer

class GetPlanes(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company = Company.objects.get(owner=owner)
                plane_qs = Planes.objects.all()
                serializer = PlaneSerializer(plane_qs, many=True)
                return Response(serializer.data)
            
            return Response({'message':'user not found '}, status = 403)
        return Response({'message':'user not found '}, status = 403)
    

class BuyPlane(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            if Owner.objects.filter(user=user).exists():
                owner = Owner.objects.get(user=user)
                company = Company.objects.get(owner=owner)
                data = request.data
                plane = data.get('plane_id')
                plane = Planes.objects.get(id=plane)
                wallet = Wallet.objects.get(owner=owner)
                if wallet.balance < plane.price:
                    return Response({'message':'you don\'t have enough money to buy this plan'}, status = 403)
                if wallet.balance >= decimal.Decimal(wallet.balance) - plane.price:
                    companyPlaneData = {
                    'plane': plane.id,
                    'company': company.id,
                        }
                    serializer = CompanyPlaneSerializer(data = companyPlaneData)
                    if serializer.is_valid(): 
                        serializer.save()
                        wallet.balance = decimal.Decimal(wallet.balance) - plane.price
                        wallet.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message':'you don\'t have enough money to buy this plan'})
            return Response({'message':'you are not authorized to make this action'},status=403)
        return Response({'message':'user not found '}, status = 403)
