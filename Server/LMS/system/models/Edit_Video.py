from django.db import models
from system.models.Video import Video

class EditVideo(models.Model):
  video = models.ForeignKey(Video, on_delete=models.CASCADE)
  file_path = models.FilePathField()
  description = models.TextField()
  EDITION_STATES = [
    ('E', 'Editing'),
    ('R', 'Ready'),
    ('P', 'Published')
  ]
  state = models.CharField(max_length=1, choices=EDITION_STATES)
  edition_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.file_path