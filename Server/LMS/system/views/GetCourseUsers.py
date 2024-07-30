#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#models 
from system.models.Course import Course
from authentication.models.User import User 

#django 
from django.shortcuts import get_object_or_404
from django.db.models import Q, F, Value 
#serializers 
from system.serializers.CourseUserSerializer import UserSerializer


class GetCourseUsers(APIView):

      def get(self,request,*args,**kwargs):
            course = get_object_or_404(Course , id = kwargs['id'])
            company = course.company
            # Fetch the company and course 

            # Fetch all users associated with the company
            users = User.objects.filter(
                Q(is_trainer = True,trainer__trainer_contract__employed = True,trainer__trainer_contract__company=company) | 
                Q(is_trainee =True,trainee__trainee_contract__employed = True,trainee__trainee_contract__company=company) | 
                Q(is_admin = True,admin__admin_contract__employed = True,admin__admin_contract__company=company)
            ).distinct()
            
            user_data = []

            for user in users:
                role = None
                is_participant = False
                completion_date = None 

                if hasattr(user, 'trainer'):
                    if course.trainers.filter(trainer=user.trainer).exists():
                        role = 'trainer'
                        is_participant = True
 
                if hasattr(user, 'trainee'):
                    trainee_contract = course.trainees.filter(trainee=user.trainee).first()
                    
                    if trainee_contract:
                        role = 'trainee' if role is None else role
                        is_participant = True
                        completion_date = trainee_contract.enrollment_set.get(course = course).completed_at
               
               
                user_data.append({
                     'id':user.id,
                    'username': user.username,
                    'email':user.email,
                    'role': role,
                    'is_participant': is_participant,
                    'completion_date': completion_date
                })

            return Response(user_data)