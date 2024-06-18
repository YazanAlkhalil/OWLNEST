from django.db import models
from authentication.admin import User

class trainee(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


class traineeContract(models.Model):
    traineeContract_id = models.IntegerField(primary_key=True)
    trainee_id = models.ForeignKey(trainee,on_delete=models.CASCADE)
    company_id = models.IntegerField()
    joining_date = models.DateField(auto_now=True)


class traineeNotfication(models.Model):
    traineeNotfication_id = models.IntegerField(primary_key=True)
    traineeContract_id = models.ForeignKey(traineeContract,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)



