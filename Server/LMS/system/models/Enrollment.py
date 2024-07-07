#django
from django.db import models  
#models
from system.models.Course import Course 
from system.models.Trainee_Contract import Trainee_Contract 

class Enrollment(models.Model):
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      trainee_contract = models.ForeignKey(Trainee_Contract, on_delete= models.CASCADE)
      join_date = models.DateField(auto_now_add=True)
      progress = models.DecimalField(max_digits=5,decimal_places=2,default=0.0)
      completed = models.BooleanField(default=False)
      completed_at = models.DateField(null = True,blank = True)
      xp_avg = models.DecimalField(max_digits=5,decimal_places=2 , default=0.0)
      
      def __str__(self) -> str:
            return f"{self.trainee_contract.trainee.user.username}  || {self.course.name}"
      
      class Meta:
            unique_together = ['trainee_contract', 'course']