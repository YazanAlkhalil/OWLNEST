from django.db import models
from authentication.admin import User

class trainer(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


class trainerContract(models.Model):
    trainerContract_id = models.IntegerField(primary_key=True)
    trainer_id = models.ForeignKey(trainer,on_delete=models.CASCADE)
    company_id = models.IntegerField()
    joining_date = models.DateField(auto_now=True)


class trainerNotfication(models.Model):
    trainerNotfication_id = models.IntegerField(primary_key=True)
    trainerContract_id = models.ForeignKey(trainerContract,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)