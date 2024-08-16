from django.db import models
from system.models.Company import Company
from system.models.Planes import Planes 


class Company_Planes(models.Model):
      company = models.ForeignKey(Company, on_delete=models.CASCADE)
      plane = models.ForeignKey(Planes , on_delete=models.CASCADE)
      purchased_at = models.DateField(auto_now_add=True)
      current_courses_number = models.IntegerField(default=0)
      is_active = models.BooleanField(default=True)
      is_full = models.BooleanField(default=False)