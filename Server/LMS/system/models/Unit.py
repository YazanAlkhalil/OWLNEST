from django.db import models
from system.models.Course import Course

class Unit(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  pref_description = models.TextField()
  order = models.IntegerField(default=0)
  
  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['title']