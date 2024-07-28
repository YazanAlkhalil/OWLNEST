#DRF 
from rest_framework import serializers

#system models 
from system.models.Enrollment import Enrollment
from system.models.Grade import Grade
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Finished_Content import Finished_Content 

#django 
from django.db.models import Q , Sum
from datetime import datetime, timedelta
class TraineeMainDashboard(serializers.Serializer):
      '''
      get total xp : trainee_contract 
      get training time : (pending)
      get rank : number of traninees who have more xp + 1
      get finished courses : enrollment completed = true
      get in progress courses : enrollment who finished at least one content not all
      get pending courses : enrollment who hasn't finish any content yet 
      '''
      xp = serializers.DecimalField(max_digits=5,decimal_places=2)
      training_time = serializers.TimeField()
      rank = serializers.IntegerField()
      daily_xp = serializers.ListField(child = serializers.DictField())
      finished_courses = serializers.IntegerField()
      in_progress_courses = serializers.IntegerField()
      pending_courses = serializers.IntegerField()
    #  skills = serializers.ListField()

      def to_internal_value(self, data):
          dashboard = dict()
          trainee_contract = data["trainee_contract"] 
          # xp
          total_xp = trainee_contract.total_xp or 0 
          dashboard['xp'] = total_xp
         # training time  
          total_time = self.get_training_time(trainee_contract)
          dashboard['training_time'] = total_time
                   
          #rank
          rank = Trainee_Contract.objects.filter(
              total_xp__gt=total_xp
          ).distinct().count() + 1 
          dashboard['rank'] = rank
          #finished courses number
          finished_courses = Enrollment.objects.filter(trainee_contract = trainee_contract , completed=True ).count()
          dashboard['finished_courses'] = finished_courses
          
          #in progress courses number
          in_progress_courses = trainee_contract.enrollment_set.filter(
              Q(finished_content__isnull=False) | Q(grade__isnull=False)
          ).filter(completed = False).distinct().count()
          dashboard['in_progress_courses'] = in_progress_courses
          #pending courses number
          pending_courses = trainee_contract.enrollment_set.filter(
              finished_content__isnull=True, grade__isnull=True
          ).count()
          dashboard['pending_courses'] = pending_courses
          dashboard['daily_xp'] = self.get_daily_xp(trainee_contract)
          return dashboard
      


      def get_daily_xp(self, trainee_contract):
        today = datetime.today()
        daily_xp = []

        for i in range(7):
            day = today - timedelta(days=i)
            start_of_day = datetime.combine(day, datetime.min.time())
            end_of_day = datetime.combine(day, datetime.max.time())
           
            finished_content_xp = Finished_Content.objects.filter(
                enrollment__trainee_contract=trainee_contract,
                finished_at__range=(start_of_day, end_of_day)
            ).count() * 10 
            
       
            grade_xp = Grade.objects.filter(
                enrollment__trainee_contract=trainee_contract,
                taken_at__range=(start_of_day, end_of_day)
            ).aggregate(total_xp=Sum('xp'))['total_xp'] or 0

           
            day_xp = finished_content_xp + grade_xp
            
            daily_xp.append({
                "day": day.strftime("%a").upper(),
                "xp": day_xp
            })

        return daily_xp
      
      def get_training_time(self, trainee_contract):
        total_time = timedelta()
        enrollments = Enrollment.objects.filter(trainee_contract=trainee_contract)
        for enrollment in enrollments:
            total_time += enrollment.training_time
        days = total_time.days
        hours, remainder = divmod(total_time.seconds, 3600)
        minutes = remainder // 60
        formatted_time = f"{days:02}:{hours:02}:{minutes:02}"
        return formatted_time