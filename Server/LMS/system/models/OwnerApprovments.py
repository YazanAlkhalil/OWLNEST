from django.db import models


#models 
from system.models.Owner import Owner
from system.models.Course import Course



class OwnerApprovment(models.Model):
      owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
      course = models.ForeignKey(Course,on_delete=models.CASCADE)

      def __str__(self) -> str:
            return f"{self.admin_contract.admin.user.username} approvment for course {self.course.name}"