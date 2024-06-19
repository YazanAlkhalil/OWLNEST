from django.db import models
from authentication.models import User
from system.models.Trainee_Contract import Trainee_Contract

class Trainee_Notfication(models.Model):
    contract = models.ForeignKey(Trainee_Contract,on_delete=models.CASCADE)
    description = models.TextField()
