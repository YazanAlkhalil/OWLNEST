from django.db import models
from system.models.Unit import Unit

class EditUnit(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  pref_description = models.TextField()
  EDITION_STATES = [
    ('E', 'Editing'),
    ('R', 'Ready'),
    ('P', 'Published')
  ]
  state = models.CharField(max_length=1, choices=EDITION_STATES)
  edition_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
