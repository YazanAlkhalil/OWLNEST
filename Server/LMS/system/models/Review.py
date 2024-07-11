from django.db import models
from system.models.Enrollment import Enrollment
from system.models.Course import Course
class Review(models.Model):
      course = models.ForeignKey(Course,on_delete=models.CASCADE)
      enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
      description = models.TextField(max_length=1024)
      rate = models.DecimalField(max_digits=3,decimal_places=2)
      created_at = models.DateTimeField(auto_now_add=True)
      def __str__(self) -> str:
            return f"{self.enrollment.trainee_contract.trainee.user.username} || {self.description}"
      
      class Meta:
            ordering = ['-created_at']
            unique_together = ['course' , 'enrollment']
