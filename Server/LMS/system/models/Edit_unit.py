from django.db import models
from system.models.Unit import Unit

class EditUnit(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  pref_description = models.TextField()
  EDITION_STATES = [
    ('PR', 'InProgress'),
    ('PE', 'Pending'),
    ('PU', 'Published')
  ]
  state = models.CharField(max_length=2, choices=EDITION_STATES)
  edition_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
