from django.db import models

class Temp_Unit(models.Model):
    unit = models.OneToOneField('Unit', on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    EDITION_STATES = [
        ('PR', 'InProgress'),
        ('PE', 'Pending'),
        ('PU', 'Published'),
        ('DE', 'Delete'),
    ]
    state = models.CharField(max_length=2, choices=EDITION_STATES, default='PR')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        unique_together = ['unit','order']
        