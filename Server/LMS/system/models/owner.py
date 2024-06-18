from django.db import models
from authentication.admin import User

class owner(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class traineeNotfication(models.Model):
    ownerNotfication_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(owner,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)


class company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(owner,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=75)
    company_email = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
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
    location = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=10)
    SIZE_CHOICES = [
        ('S','small'),
        ('M','medium'),
        ('L','large'),
    ]
    company_size = models.CharField(max_length=1,choices=SIZE_CHOICES,default='S')
    description = models.CharField(max_length=255)
    created_day = models.DateField(auto_now=True)


class plane(models.Model):
    plane_id = models.IntegerField(primary_key=True)
    company_id = models.ForeignKey(company,on_delete=models.CASCADE)
    courses_number = models.IntegerField
    price = models.DecimalField(6,2)