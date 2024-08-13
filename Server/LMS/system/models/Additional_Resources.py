from django.db import models

#models 
from system.models.Course import Course
class Additional_Resources(models.Model):
      course = models.OneToOneField(Course , on_delete= models.CASCADE,related_name="resource")
      text = models.TextField()
      def __str__(self):
        return self.text[10:]