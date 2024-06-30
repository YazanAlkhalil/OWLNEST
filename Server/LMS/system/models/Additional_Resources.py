from django.db import models

class Additional_Resources(models.Model):
  resource_link = models.URLField()
  def __str__(self):
    return self.resource_link