from django.db import models
from system.models.Content import Content

class Pdf(models.Model):
  content = models.ForeignKey(Content, on_delete=models.CASCADE)
  file_path = models.FileField()
  def __str__(self):
    return self.file_path