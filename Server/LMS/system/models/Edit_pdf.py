from django.db import models
from system.models.Pdf import Pdf

class EditPdf(models.Model):
  pdf = models.ForeignKey(Pdf, on_delete=models.CASCADE)
  file_path = models.FileField()
  EDITION_STATES = [
    ('PR', 'InProgress'),
    ('PE', 'Pending'),
    ('PU', 'Published')
  ]
  state = models.CharField(max_length=2, choices=EDITION_STATES)
  edition_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.file_path