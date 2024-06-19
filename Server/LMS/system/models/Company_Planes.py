from django.db import models
from system.models.Company import Company
from system.models.Planes import Planes


class Company_Planes(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    plane = models.ForeignKey(Planes , on_delete=models.CASCADE)