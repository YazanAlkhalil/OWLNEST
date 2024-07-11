from django.db import models
from authentication.models.User import User

class Admin(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username