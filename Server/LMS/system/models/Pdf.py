from django.db import models
from ..models.Content import Content 
class Pdf(models.Model):
    # file will be uploaded to MEDIA_ROOT/pdf_<pdf-id>/<filename>
    def pdf_file_path(instance, filename):
        return f'pdf_{instance.id}/{filename}'
    content = models.OneToOneField(Content, on_delete=models.CASCADE, null=True) 
    file_path = models.FileField(upload_to=pdf_file_path)
    def __str__(self):
        return self.file_path