from django.db import models

#models 
from system.models.DraftQuestion import DraftQuestion

class DraftAnswer(models.Model):
      question = models.ForeignKey(DraftQuestion,on_delete=models.CASCADE)
      answer = models.CharField(max_length=255)
      is_correct = models.BooleanField(default=False) 
      def __str__(self) -> str:
            return f"{self.answer}"