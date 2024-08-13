from django.db import models

#models 
from system.models.DraftContent import DraftContent

class DraftVideo(models.Model):
      content = models.OneToOneField(DraftContent,on_delete=models.CASCADE)
      file = models.FileField(upload_to="videos") 
      description = models.TextField(null= True,blank = True)
      def __str__(self) -> str:
            return f"{self.content.title}"