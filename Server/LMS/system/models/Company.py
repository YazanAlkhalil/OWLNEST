from django.db import models
from authentication.models import User
from system.models.Owner import Owner
from system.models.Trainee import Trainee
from system.models.Trainer import Trainer
from system.models.Admin import Admin
class Company(models.Model):
    owner = models.OneToOneField(Owner,on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    email = models.CharField(max_length=255,unique=True)
    def logo_path(instance, filename):
        return f'logo_{instance.id}/{filename}'
    logo = models.ImageField(upload_to='images', null=True, blank=True)
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
    phone = models.CharField(max_length=10)
    SIZE_CHOICES = [
        ('S','small'),
        ('M','medium'),
        ('L','large'),
    ]
    size = models.CharField(max_length=1,choices=SIZE_CHOICES,default='S')
    description = models.CharField(max_length=255)
    created_day = models.DateField(auto_now_add=True)
    trainees =  models.ManyToManyField(Trainee,through='system.Trainee_Contract')
    trainers =  models.ManyToManyField(Trainer,through='system.Trainer_Contract')
    admins =  models.ManyToManyField(Admin,through='system.Admin_Contract')
    def __str__(self) -> str:
        return self.name