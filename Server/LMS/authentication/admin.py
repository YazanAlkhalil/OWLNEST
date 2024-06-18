from django.contrib import admin

from django.contrib import admin
from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    birthday = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    COUNTRY_CHOICES = [
        ('DZ', 'Algeria'),
        ('BH', 'Bahrain'),
        ('EG', 'Egypt'),
        ('IQ', 'Iraq'),
        ('JO', 'Jordan'),
        ('KW', 'Kuwait'),
        ('LB', 'Lebanon'),
        ('LY', 'Libya'),
        ('MR', 'Mauritania'),
        ('MA', 'Morocco'),
        ('OM', 'Oman'),
        ('PS', 'Palestine'),
        ('QA', 'Qatar'),
        ('SA', 'Saudi Arabia'),
        ('SD', 'Sudan'),
        ('SY', 'Syria'),
        ('TN', 'Tunisia'),
        ('AE', 'United Arab Emirates'),
        ('YE', 'Yemen'),
    ]
    country = models.CharField(max_length=2,choices=COUNTRY_CHOICES,default='SY')
    is_trainee = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    joining_date = models.DateField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
