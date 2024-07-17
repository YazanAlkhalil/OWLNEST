from django.db import models
from system.models.Temp_unit import Temp_Unit
# models
from ..models.Content import Content

class Temp_Content(models.Model):
    temp_unit = models.ForeignKey(Temp_Unit, on_delete=models.CASCADE)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=256)
    order = models.IntegerField(default=0)
    is_video = models.BooleanField(default=False)
    is_pdf = models.BooleanField(default=False)
    is_test = models.BooleanField(default=False)    
    EDITION_STATES = [
        ('PR', 'InProgress'),
        ('PE', 'Pending'),
        ('PU', 'Published'),
        ('DE', 'Delete'),
    ]
    state = models.CharField(max_length=2, choices=EDITION_STATES)

    def __str__(self):
        return f"{self.title}||{self.unit.title}||{self.unit.course.name}"
    
    class Meta:
        ordering = ['order']