from django.db import models
from authentication.models.User import User

class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
        
    def __str__(self) -> str:
            return f"{self.user.username}"