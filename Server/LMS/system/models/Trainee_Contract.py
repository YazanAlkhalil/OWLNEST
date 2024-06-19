from django.db import models
from authentication.models import User
from system.models import Trainee,Company

class Trainee_Contract(models.Model):
    trainee = models.ForeignKey(Trainee,on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now=True)