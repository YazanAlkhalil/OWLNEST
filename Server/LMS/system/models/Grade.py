from django.db import models
from system.models.Enrollment import Enrollment
from system.models.Test import Test

class Grade(models.Model):
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
      test = models.ForeignKey(Test,on_delete=models.CASCADE)
      score = models.DecimalField(max_digits=4,decimal_places=2)
      taken_at = models.DateField(auto_now_add=True)
      xp = models.DecimalField(max_digits=5,decimal_places=2,null = True,blank=True)
    
      def __str__(self) -> str:
            return f"{self.enrollment.trainee_contract.trainee.user.username}|| {self.enrollment.course.name}  || {self.test.content}"
      
      class Meta:
            unique_together = ['test','enrollment']