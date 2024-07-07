from django.db import models
from system.models.Trainer import Trainer
from system.models.Company import Company

class Trainer_Contract(models.Model):
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now=True)
  
    def __str__(self):
        return f'trainer contract for trainer {self.trainer}'