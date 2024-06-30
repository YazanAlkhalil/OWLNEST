from django.db import models
from system.models.Company import Company
from system.models.Admin_Contract import Admin_Contract
from system.models.Additional_Resources import Additional_Resources
from system.models.Trainer_Contract import Trainer_Contract

class Course(models.Model):
    # file will be uploaded to MEDIA_ROOT/course_<course-id>/<filename>
    def course_image_path(instance, filename):
        return f'course_{instance.id}/{filename}'
    # difining the model fields
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    admin_contract = models.ForeignKey(Admin_Contract, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    pref_description = models.TextField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=course_image_path, null=True, blank=True)
    expected_time = models.CharField(max_length=16)
    publish_date = models.DateField(auto_now_add=True)
    additional_resources = models.ManyToManyField(Additional_Resources)
    trainers = models.ManyToManyField(Trainer_Contract, through='system.Trainer_Contract_Course')
    # when call an instance show just its name
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']