from django.db import models
from system.models.Company import Company
from system.models.Company_Planes import Company_Planes
from system.models.Planes import Planes
from system.models.Course import Course
from authentication.models.User import User


class Courses_In_Plane(models.Model):
      company_plane = models.ForeignKey(Company_Planes, on_delete=models.CASCADE)
      course = models.OneToOneField(Course, on_delete=models.CASCADE)
      added_in = models.DateField(auto_now_add=True)
      cources_number = models.IntegerField(default=0)