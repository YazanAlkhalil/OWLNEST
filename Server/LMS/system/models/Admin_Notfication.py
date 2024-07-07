from django.db import models
from system.models.Admin_Contract import Admin_Contract


class Admin_Notfication(models.Model):
    admin_contract = models.ForeignKey(Admin_Contract,on_delete=models.CASCADE)
    description = models.TextField()