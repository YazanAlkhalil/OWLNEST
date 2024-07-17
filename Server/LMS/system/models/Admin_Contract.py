from django.db import models 
from system.models.Admin import Admin
from system.models.Company import Company

class Admin_Contract(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.admin.user.username} || {self.company.name}"