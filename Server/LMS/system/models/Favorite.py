from django.db import models
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Enrollment import Enrollment

class Favorite(models.Model):
      trainee_contract = models.ForeignKey(Trainee_Contract,on_delete= models.CASCADE)
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
      
      def __str__(self) -> str:
            return f"{self.trainee_contract.trainee.user.username}  || {self.enrollment.course.name}"
      
      class Meta:
            unique_together = ['trainee_contract','enrollment']

