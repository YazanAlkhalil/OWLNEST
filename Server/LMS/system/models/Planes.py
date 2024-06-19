from django.db import models
from authentication.models import User

class Planes(models.Model):
    plane_name = models.CharField(max_length=55)
    subscription_term = models.DurationField()
    courses_number = models.IntegerField()
    additional_course_price = models.DecimalField()