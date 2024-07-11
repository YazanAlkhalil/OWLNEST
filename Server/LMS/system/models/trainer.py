from django.db import models
from authentication.models.User import User

class Trainer(models.Model):
    trainer = models.OneToOneField(User,on_delete=models.CASCADE)
        
    def __str__(self) -> str:
            return f"{self.user.username} "