from django.db import models
from authentication.models import User
from system.models.Owner import Owner


class Owner_Notfication(models.Model):
    user = models.ForeignKey(Owner,on_delete=models.CASCADE)
    description = models.TextField()