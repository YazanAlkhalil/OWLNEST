from django.db import models
from system.models.Trainee_Contract import Trainee_Contract

class Trainee_Notification(models.Model):
    trainee_contract = models.ForeignKey(Trainee_Contract,on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateField(auto_now_add=True)
      