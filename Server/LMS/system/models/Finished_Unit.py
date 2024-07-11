from django.db import models 
from system.models.Enrollment import Enrollment
from system.models.Unit import Unit


class Finished_Unit(models.Model):
      unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
      finished_at = models.DateField(auto_now_add=True)

      def __str__(self) -> str:
            return f"{self.enrollment.trainee_contract.trainee.user.username} || {self.unit.title} || {self.enrollment.course.name}"
  
      class Meta:
            unique_together = ['unit','enrollment']