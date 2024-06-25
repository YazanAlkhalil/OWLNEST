from django.db import models
from system.models.Company import Company

class Course(models.Model):
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  name = models.CharField(max_length=256)
  description = models.TextField()
  image_path = models.CharField(max_length=512)
  expected_time = models.CharField(max_length=16)
  publish_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']