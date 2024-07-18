from django.db import models
from system.models.Owner import Owner
from authentication.models.User import User
class Owner_Notification(models.Model):
      from_user = models.ForeignKey(User,on_delete=models.CASCADE )
      owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
      content = models.TextField()
      is_read = models.BooleanField(default=False)
      sent_at = models.DateField(auto_now_add=True)
