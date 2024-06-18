from django.db import models
from authentication.admin import User

class admin(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


class adminContract(models.Model):
    adminContract_id = models.IntegerField(primary_key=True)
    admin_id = models.ForeignKey(admin,on_delete=models.CASCADE)
    company_id = models.IntegerField()
    joining_date = models.DateField(auto_now=True)


class adminNotfication(models.Model):
    adminNotfication_id = models.IntegerField(primary_key=True)
    adminContract_id = models.ForeignKey(adminContract,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)