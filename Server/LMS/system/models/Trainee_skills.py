from django.db import models
from system.models.Skill import Skill
from system.models.Enrollment import Enrollment
class Trainee_Skills(models.Model):
      enrollment = models.ForeignKey(Enrollment ,on_delete= models.CASCADE)
      skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
      rate = models.DecimalField(max_digits=3,decimal_places=2)
