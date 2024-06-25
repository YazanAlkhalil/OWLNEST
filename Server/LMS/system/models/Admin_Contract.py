from django.db import models
from authentication.models import User
from system.models.admin import Admin
from system.models.Company import Company

class Admin_Contract(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now=True)