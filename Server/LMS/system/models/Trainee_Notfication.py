from django.db import models
from authentication.models import User
from system.models import Trainee_Contract

class Trainee_Notfication(models.Model):
    contract = models.ForeignKey(Trainee_Contract,on_delete=models.CASCADE)
    description = models.TextField()
