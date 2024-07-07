from django.db import models
from system.models.Course import Course
from system.models.Trainer_Contract import Trainer_Contract

class Trainer_Contract_Course(models.Model):
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      trainer_contract = models.ForeignKey(Trainer_Contract, on_delete=models.CASCADE)
      start_date = models.DateField(auto_now_add=True)
      def __str__(self):
            return f'trainers for {self.course} course'
      
      class Meta:
            unique_together = ['trainer_contract','course']
      