from django.db import models
from authentication.models import User

class Trainee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)