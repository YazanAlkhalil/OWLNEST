from django.db import models 

#models 
from system.models.Course import Course

class DraftUnit(models.Model):
      course = models.ForeignKey(Course, on_delete= models.CASCADE,related_name="draft_units")
      title = models.CharField(max_length=255)
      order = models.BigIntegerField()

      class Meta: 
            ordering = ['order']