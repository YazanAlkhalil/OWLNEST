from django.db import models
from authentication.models import User
from system.models import Admin_Contract


class Admin_Notfication(models.Model):
    contract = models.ForeignKey(Admin_Contract,on_delete=models.CASCADE)
    description = models.TextField()