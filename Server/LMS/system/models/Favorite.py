from django.db import models
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Enrollment import Enrollment

class Favorite(models.Model):
      trainer_contract = models.ForeignKey(Trainee_Contract,on_delete= models.CASCADE)
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
