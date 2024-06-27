from django.db import models
from system.models.Enrollment import Enrollment
from system.models.Test import Test

class Grade(models.Model):
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
      test = models.ForeignKey(Test,on_delete=models.CASCADE)
      score = models.DecimalField(max_digits=3,decimal_places=2)
      taken_at = models.DateField(auto_now_add=True)
