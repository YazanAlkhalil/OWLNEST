from django.db import models
from system.models.Unit import Unit

class Content(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    expected_time = models.CharField(max_length=16)
    order = models.IntegerField(default=0)
    is_video = models.BooleanField(default=False)
    is_pdf = models.BooleanField(default=False)
    is_test = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}||{self.unit.title}||{self.unit.course.name}"
    
    class Meta:
        ordering = ['order']