from django.db import models 

#models 
from system.models.DraftUnit import DraftUnit

class DraftContent(models.Model):
      unit = models.ForeignKey(DraftUnit, on_delete= models.CASCADE,related_name="contents")
      title = models.CharField(max_length=255)
      order = models.BigIntegerField()
      is_video = models.BooleanField(default=False)
      is_pdf = models.BooleanField(default=False)
      is_test = models.BooleanField(default=False)

      class Meta: 
            ordering = ['order']

      