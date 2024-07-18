from django.db import models
from system.models.Trainer_Contract import Trainer_Contract
from authentication.models.User import User
class Trainer_Notfication(models.Model):
      from_user = models.ForeignKey(User,on_delete=models.CASCADE )
      trainer_contract = models.ForeignKey(Trainer_Contract,on_delete=models.CASCADE)
      content =  models.TextField()
      is_read = models.BooleanField(default=False)
      sent_at = models.DateField(auto_now_add=True)
      