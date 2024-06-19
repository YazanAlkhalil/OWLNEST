from django.db import models
from authentication.models import User

class Trainer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

