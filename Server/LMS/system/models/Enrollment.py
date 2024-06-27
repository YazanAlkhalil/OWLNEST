from django.db import models  
from system.models.Course import Course 
from system.models.Trainee_Contract import Trainee_Contract
class Enrollment(models.Model):
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      trainer_contract = models.ForeignKey(Trainee_Contract, on_delete= models.CASCADE)
      join_date = models.DateField(auto_now_add=True)
      progress = models.DecimalField(max_digits=3,decimal_places=2)
      completed = models.BooleanField(default=False)
      completed_at = models.DateField()
      xp_avg = models.DecimalField(max_digits=3,decimal_places=2)
