from django.db import models


#models 
from system.models.Admin_Contract import Admin_Contract
from system.models.Course import Course



class AdminApprovment(models.Model):
      admin_contract = models.ForeignKey(Admin_Contract,on_delete=models.CASCADE)
      course = models.ForeignKey(Course,on_delete=models.CASCADE)

      def __str__(self) -> str:
            return f"{self.admin_contract.admin.user.username} approvment for course {self.course.name}"