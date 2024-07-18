from django.db import models
from system.models.Trainee import Trainee
from system.models.Company import Company

class Trainee_Contract(models.Model):
    trainee = models.ForeignKey(Trainee,on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    total_xp = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    joining_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.trainee.user.username} || {self.company.name}"