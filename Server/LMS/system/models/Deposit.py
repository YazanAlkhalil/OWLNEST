from django.core.validators import MinValueValidator
from django.db import models
from system.models.Wallet import Wallet

class Deposit(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField(null=False, validators=[MinValueValidator(0.01)])
    deposited_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if this is a new deposit
            self.wallet.balance += self.amount
            self.wallet.save()
        super().save(*args, **kwargs)
