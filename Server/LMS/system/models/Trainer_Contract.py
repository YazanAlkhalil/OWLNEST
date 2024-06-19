from django.db import models
from authentication.models import User
from system.models import Trainer,Company

class Trainer_Contract(models.Model):
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now=True)