from rest_framework import serializers
from system.models.Wallet import Wallet
from system.models.Deposit import Deposit
from system.models.Withdraw import Withdraw

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id','owner']


class DepositeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['id','wallet','amount']


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ['id','wallet','amount']

