from django.db import models
from system.models.Content import Content

class Test(models.Model):
  content = models.ForeignKey(Content, on_delete=models.CASCADE)
  full_mark = models.FloatField()
  full_xp = models.FloatField()

  def __str__(self):
    return f"Test for {self.content.title}"