from django.db import models
from system.models.Wallet import Wallet

class Withdraw(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    amount = models.FloatField()
    withdrawn_at = models.DateTimeField(auto_now_add=True)