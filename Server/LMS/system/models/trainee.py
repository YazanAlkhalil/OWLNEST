from django.db import models
from authentication.models.User import User

class Trainee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)