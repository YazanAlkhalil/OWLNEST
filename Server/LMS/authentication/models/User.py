from django.contrib import admin
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
 

class User(AbstractUser):
        username = models.CharField(max_length=255)
        email = models.CharField(max_length=255,unique=True)
        password = models.CharField(max_length=255)
        phone = models.CharField(max_length=10,null =True,blank = True)
        birthday = models.DateField(null =True,blank = True)
        GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
        ]
        gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null =True,blank = True)
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
        otp = models.CharField(max_length=6,null =True,blank = True)
        otp_verified = models.BooleanField(default=False)
        joining_date = models.DateField(auto_now_add=True)
        image = models.ImageField(null= True,blank =True)
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
        objects = CustomUserManager()

        def __str__(self) -> str:
             return self.username