#DRF 
from rest_framework import serializers
#system models 
from system.models.Course import Course
from system.models.Enrollment import Enrollment
from system.models.Content import Content
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade
#django 
from django.db.models import Avg, Count, Sum
from django.utils.timezone import now
#time 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class CourseReportSerializer(serializers.Serializer):
      '''
      1- we will pass course instance via view 
        to the serializer to handle the get
        method request to present the course
        dashboard
      2- select_related used for (OneToOne , ForeignKey)
      3- prefetch_related used for (ManyToMany) 
      ''' 

      admin_username = serializers.CharField()
      number_of_trainees_in_progress = serializers.IntegerField()
      trainees_complete = serializers.IntegerField()
      avg_grade = serializers.FloatField()
      trainers_number = serializers.IntegerField()
      graph = serializers.ListField()

      

      def to_internal_value(self, data): 
            '''
            dashboard dictionary containes admin/owner dashboard information
            '''
            dashboard = dict()
            #get the course object by params
            course = Course.objects.select_related(
                      'admin_contract__admin__user',
                      'company'
                  ).prefetch_related(
                      'company__admin_contract_set',
                      'enrollment_set__finished_content_set',
                      'enrollment_set__trainee_contract__trainee__user'
                  ).get(id=data.id)
            #get admin name      
            admin = course.admin_contract.admin.user.username
            dashboard["admin_username"] = admin
            # number of trainees in progress
            finished_contents = Finished_Content.objects.filter(enrollment__course=course) 
            trainees_in_progress = finished_contents.values(
                'enrollment__trainee_contract__trainee'
            ).annotate(
                finished_content_count=Count('id')
            ).filter(finished_content_count__gt=0, enrollment__completed = False)
            
            dashboard["number_of_trainees_in_progress"] = trainees_in_progress.count()
            # number of trainees who completed the course
            trainees_complete = Enrollment.objects.filter(
                course=course,
                completed = True
            ).count()
            
            dashboard["trainees_complete"] = trainees_complete

            # average grade for trainees who completed the course
            avg_grade = Grade.objects.filter(
                    enrollment__course=course,
                    enrollment__completed=True,
                    test__content__unit__course=course
                ).aggregate(Avg('score'))['score__avg'] or 0
            
            dashboard["avg_grade"] = avg_grade 
            trainers_number = course.trainers.all().count()
            dashboard['trainers_number'] = trainers_number
            
                     
            now = datetime.now() 
            months = [(now - relativedelta(months=i)).strftime('%Y-%m') for i in range(12)]
            print(months) 
            graph = []
            
            for month in months:
                year, month = month.split('-')
                
               
                start_date = datetime(int(year), int(month), 1)
                end_date = start_date + relativedelta(months=1) - timedelta(seconds=1)
                print("start",start_date)
                print("end",end_date)
             
                grade_xp = Grade.objects.filter(
                    enrollment__course=course,
                    taken_at__range=(start_date, end_date)
                ).aggregate(total_xp=Sum('xp'))['total_xp'] or 0
                 
                content_xp = Finished_Content.objects.filter(
                    enrollment__course=course,
                    finished_at__range=(start_date, end_date)
                ).aggregate(total_xp=Sum('xp'))['total_xp'] or 0
                 
                total_xp = grade_xp + content_xp
                graph.append({'month': start_date.strftime('%b'), 'xp': total_xp})

            dashboard['graph'] = graph
            return dashboard 