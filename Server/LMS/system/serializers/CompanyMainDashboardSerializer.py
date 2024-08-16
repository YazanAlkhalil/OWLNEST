#DRF 
from rest_framework import serializers
#system models 
from system.models.Company import Company
from system.models.Enrollment import Enrollment  
#django 
from django.db.models import Avg, Count, Sum
from django.utils.timezone import now
#time 
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta

#time 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class AdminMainDashboardSerializer(serializers.Serializer):
      owner = serializers.CharField()
      trainees = serializers.IntegerField()
      trainers = serializers.IntegerField()
      admins   = serializers.IntegerField()
      total_completions = serializers.IntegerField()
      graph = serializers.ListField()

      def to_internal_value(self, instance):
            


            dashboard = dict()
            
            # Owner
            dashboard["owner"] = instance.owner.user.username
            
            # Trainees
            trainees = instance.trainees.filter(trainee_contract__employed=True).count()
            dashboard["trainees"] = trainees 
            
            # Trainers
            trainers = instance.trainers.filter(trainer_contract__employed=True).count()
            dashboard["trainers"] = trainers
            
            # Admins
            admins = instance.admins.filter(admin_contract__employed=True).count()
            dashboard["admins"] = admins
            dashboard["total_completions"] = Enrollment.objects.filter(course__company = instance,completed = True).count()
            now = datetime.now() 
            months = [(now - relativedelta(months=i)).strftime('%Y-%m') for i in range(12)] 
            graph = []
            
            for month in months:
                year, month = month.split('-')
                start_date = datetime(int(year), int(month), 1)
                end_date = start_date + relativedelta(months=1) - timedelta(seconds=1)
                completions = Enrollment.objects.filter(
                    course__company= instance,
                    completed_at__range=(start_date, end_date)
                ).count() 
                graph.append({'month': start_date.strftime('%b'), 'completions': completions})
            dashboard["graph"] = graph
            return dashboard
      
 


class OwnerDashboardSerializer(AdminMainDashboardSerializer):
      balance = serializers.DecimalField(max_digits=5,decimal_places=2)
      def to_internal_value(self, instance):
          data = AdminMainDashboardSerializer.to_internal_value(self,instance)
          data["balance"] = instance.owner.wallet.balance or 0
          return data
      