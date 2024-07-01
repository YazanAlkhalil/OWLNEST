from django.db import models
from system.models.Test import Test

class Question(models.Model):
  test = models.ForeignKey(Test, on_delete=models.CASCADE)
  question = models.TextField()
  feedback = models.TextField()
  mark = models.FloatField()
  xp = models.FloatField()

  def __str__(self):
    return self.question
