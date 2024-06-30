from django.db import models
from system.models.Course import Course
from system.models.Trainer import Trainer
class Trainer_Course(models.Model):
      course = models.ForeignKey(Course,on_delete=models.CASCADE)
      trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
      start_date = models.DateField(auto_now_add=True)
