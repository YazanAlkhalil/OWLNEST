#DRF 
from rest_framework import serializers
#system models 
from system.models.Company import Company
from system.models.Enrollment import Enrollment  
#django 
from django.db.models import Avg, Count, Sum
from django.utils.timezone import now
#time 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class AdminMainDashboardSerializer(serializers.Serializer):
      owner = serializers.CharField()
      trainees = serializers.IntegerField()
      trainers = serializers.IntegerField()
      admins   = serializers.IntegerField()
      total_completions = serializers.IntegerField()
      
      def to_internal_value(self, instance):
        # Assuming instance is the `company` object
        dashboard = dict()
        
        # Owner
        dashboard["owner"] = instance.owner.user.username
        
        # Trainees
        trainees = instance.trainees.filter(trainee_contract__employed=True).count()
        dashboard["trainees"] = trainees  # No need to convert count to a string
        
        # Trainers
        trainers = instance.trainers.filter(trainer_contract__employed=True).count()
        dashboard["trainers"] = trainers
        
        # Admins
        admins = instance.admins.filter(admin_contract__employed=True).count()
        dashboard["admins"] = admins
        dashboard["total_completions"] = 12
        return dashboard