from django.db import models

#models 
from system.models.Course import Course

class DraftSkill(models.Model):
      course = models.ForeignKey(Course,on_delete=models.CASCADE) 
      skill = models.CharField(max_length=255)
      rate = models.BigIntegerField()
      def __str__(self) -> str:
            return f"{self.skill}"