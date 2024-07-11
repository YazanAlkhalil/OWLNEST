from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from authentication.serializers.userSerializer import UserSerializer
from authentication.models import User

from system.models.Owner import Owner
from system.serializers.Company import OwnerSerializer
from system.models.Deposit import Deposit
from system.serializers.Wallet import DepositeSerilaizer
from system.models.Wallet import Wallet
from system.serializers.Wallet import WalletSerializer
from authentication.authentication import decodeAccessToken

"""class DepositView(APIView):
    def post(self,request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            if user is None:
                return Response({'message': 'user not found'}, status=404)
            
            owner = Owner.objects.filter(pk=id).first()
            id = owner.id
            if owner is None:
                return Response({'message': 'owner not found'}, status=404)
            
            wallet = Wallet.objects.filter(pk=id).first()
            id = wallet.id
            if wallet is None:
                return Response({'message': 'wallet not found'}, status=404)
            
            deposit_data = request.data
            deposit_data['wallet'] = wallet
            deposit = Deposit.objects.create(**deposit_data) 
            amount = deposit_data.get('amount')
            wallet.balance += amount  
            wallet.save()

            return Response(DepositeSerilaizer(deposit).data, status=status.HTTP_201_CREATED)"""

