from django.db import models
from ..models.Content import Content 

class Test(models.Model):
      content = models.OneToOneField(Content, on_delete=models.CASCADE, null=True)
      full_mark = models.BigIntegerField(default=0)
      def __str__(self):
          return f"Test for {self.content.title}"