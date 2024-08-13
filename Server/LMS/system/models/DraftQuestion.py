from django.db import models

#models 
from system.models.DraftTest import DraftTest

class DraftQuestion(models.Model):
      quizz = models.ForeignKey(DraftTest,on_delete=models.CASCADE)
      question = models.CharField(max_length=255)
      feedback = models.CharField(max_length=255,null=True,blank=True)
      mark = models.BigIntegerField()
      def __str__(self) -> str:
            return f"{self.question}"