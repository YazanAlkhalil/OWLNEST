from django.db import models
from system.models.Content import Content

class Test(models.Model):
  content = models.ForeignKey(Content, on_delete=models.CASCADE)
  required_mark = models.IntegerField()

  def __str__(self):
    return f"Test for {self.content.title}"