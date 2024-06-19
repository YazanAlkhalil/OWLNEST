from django.db import models
from authentication.models import User
from system.models import Trainer_Contract

class Trainer_Notfication(models.Model):
    contract = models.ForeignKey(Trainer_Contract,on_delete=models.CASCADE)
    description = models.TextField()