from django.db import models 
from system.models.Enrollment import Enrollment 
from system.models.Content import Content
class Finished_Content(models.Model):
      lesson = models.ForeignKey(Content,on_delete=models.CASCADE)
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
      finished_at = models.DateField(auto_now_add = True)
      xp = models.DecimalField(max_digits = 3,decimal_places = 2 )
      
      def __str__(self) -> str:
            return f"{self.enrollment.trainee_contract.trainee.user.username}  || {self.enrollment.course.name}"