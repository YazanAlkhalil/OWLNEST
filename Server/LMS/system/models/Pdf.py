from django.db import models
from system.models.Content import Content

class Pdf(models.Model):
  content = models.ForeignKey(Content, on_delete=models.CASCADE)
  file_path = models.FilePathField()
  additional_resources = models.TextField()

  def __str__(self):
    return self.file_path