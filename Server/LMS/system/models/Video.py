from django.db import models
from ..models.Content import Content 
class Video(models.Model):
    # file will be uploaded to MEDIA_ROOT/video_<video-id>/<filename>
    def video_file_path(instance, filename):
        return f'video_{instance.id}/{filename}'
    content = models.OneToOneField(Content, on_delete=models.CASCADE, null=True) 
    file_path = models.FileField(upload_to=video_file_path)
    description = models.TextField()
    def __str__(self):
        return f'video_{self.id}'