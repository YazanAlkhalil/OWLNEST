from django.db import models
from authentication.models.User import User

class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)