from django.db import models
from system.models.Unit import Unit

class Content(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
  title = models.CharField(max_length=256)
  expected_time = models.CharField(max_length=16)
  order = models.IntegerField(default=0)
  
  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['title']