from django.db import models
from system.models.Content import Content

class Video(models.Model):
  content = models.ForeignKey(Content, on_delete=models.CASCADE)
  file_path = models.FileField()
  description = models.TextField()

  def __str__(self):
    return self.file_path