from django.db import models

class Planes(models.Model):
    plane_name = models.CharField(max_length=255)
    subscription_term = models.DurationField()
    courses_number = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)