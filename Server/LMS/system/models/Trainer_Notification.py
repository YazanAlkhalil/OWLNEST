from django.db import models
from system.models.Trainer_Contract import Trainer_Contract

class Trainer_Notfication(models.Model):
      trainer_contract = models.ForeignKey(Trainer_Contract,on_delete=models.CASCADE)
      content =  models.TextField()
      is_read = models.BooleanField(default=False)
      sent_at = models.DateField(auto_now_add=True)
      