from django.db import models
#models 
from system.models.Trainee_Contract import Trainee_Contract


class Certificate(models.Model):
      certificate = models.FileField(upload_to="certificates")
      trainee_contract = models.ForeignKey(Trainee_Contract,on_delete=models.CASCADE)

      def __str__(self) -> str:
            return f"{self.trainee_contract.trainee.user.username} || certificate"