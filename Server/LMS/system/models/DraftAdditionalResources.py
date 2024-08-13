from django.db import models

#models 
from system.models.Course import Course 

class DraftAdditionalResources(models.Model):
      course = models.ForeignKey(Course , on_delete=models.CASCADE)
      text = models.TextField()

      