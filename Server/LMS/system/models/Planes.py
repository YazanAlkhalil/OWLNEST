from django.db import models
from datetime import timedelta

class Planes(models.Model):
    plane_name = models.CharField(max_length=255)
    subscription_term = models.DurationField() 
    courses_number = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_course_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
