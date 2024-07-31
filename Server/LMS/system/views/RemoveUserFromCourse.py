#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

#models 
from system.models.Course import Course
from authentication.models.User import User


#django 
from django.shortcuts import get_object_or_404
class RemoveUserFromCourse(APIView):


      def delete(self , request,*args,**kwargs):
          if not 'user_id' in request.data.keys():
               raise ValidationError({"message":"user_id missed in the request body"})
          
          user = get_object_or_404(User,id = request.data['user_id'])
          course = get_object_or_404(Course,id= kwargs['id'])

          if user.is_trainee : 
             try:
                  trainee = course.trainees.get(trainee__user = user)
                  course.trainees.remove(trainee)
                  course.save()
                  if trainee.enrollment_set.all().count() == 0 :
                       trainee.delete()
             except : 
                  pass

          if user.is_trainer:
              try:
                   trainer = course.trainers.get(trainer__user = user)
                   course.trainers.remove(trainer)
                   course.save()  
                   if trainer.trainer_contract_course_set.all().count() == 0 : 
                        
                        trainer.delete()
              except Exception as e:
                  print(e)
          return Response({"message":"the user has been deleted from the course"})
               