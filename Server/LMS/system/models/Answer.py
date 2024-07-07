from django.db import models
from system.models.Question import Question

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  answer = models.TextField()
  is_correct = models.BooleanField(default=False)

  def __str__(self):
    return self.answer