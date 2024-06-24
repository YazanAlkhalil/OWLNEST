from django.db import models
from system.models.Pdf import Pdf

class EditPdf(models.Model):
  pdf = models.ForeignKey(Pdf, on_delete=models.CASCADE)
  file_path = models.FilePathField()
  additional_resources = models.TextField()
  EDITION_STATES = [
    ('E', 'Editing'),
    ('R', 'Ready'),
    ('P', 'Published')
  ]
  state = models.CharField(max_length=1, choices=EDITION_STATES)
  edition_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.file_path