from django.db import models

#models 
from system.models.DraftContent import DraftContent

class DraftTest(models.Model):
      content = models.OneToOneField(DraftContent,on_delete=models.CASCADE) 
      def __str__(self) -> str:
            return f"{self.content.title}"