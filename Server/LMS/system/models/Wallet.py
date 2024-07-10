from django.db import models
from system.models.Owner import Owner

class Wallet(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

