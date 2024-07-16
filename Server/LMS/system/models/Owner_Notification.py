from django.db import models
from system.models.Owner import Owner

class Owner_Notification(models.Model):
      owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
      content = models.TextField()
      is_read = models.BooleanField(default=False)
      sent_at = models.DateField(auto_now_add=True)
