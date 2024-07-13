from django.db import models

class Temp_Unit(models.Model):
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pref_description = models.TextField()
    order = models.IntegerField(default=0)
    EDITION_STATES = [
        ('PR', 'InProgress'),
        ('PE', 'Pending'),
        ('PU', 'Published'),
    ]
    state = models.CharField(max_length=2, choices=EDITION_STATES, default='PR')
    edition_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']