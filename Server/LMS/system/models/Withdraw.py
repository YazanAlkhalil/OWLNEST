from django.core.validators import MinValueValidator
from django.db import models
from system.models.Wallet import Wallet

class Withdraw(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    amount = models.FloatField(null=False, validators=[MinValueValidator(0.01)])
    withdrawn_at = models.DateTimeField(auto_now_add=True)