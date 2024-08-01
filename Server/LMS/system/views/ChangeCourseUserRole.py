#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
#models 
from system.models.Course import Course
from authentication.models.User import User
from system.models.Trainer_Contract import Trainer_Contract
from system.models.Trainer import Trainer
#django 
from django.shortcuts import get_object_or_404


class ChangeCourseUserRole(APIView):
      def post(self,request,*args,**kwargs):
          if not 'user_id' in request.data.keys():
               raise ValidationError({"message":"user_id missed"})
          if not 'role' in request.data.keys():
               raise ValidationError({"message":"role missed "}) 
          
          user = get_object_or_404(User,id = request.data["user_id"])
          course = get_object_or_404(Course, id = kwargs['id'])
          role = request.data['role']
          #change trainer to trainee
          if role.lower() == 'trainee':
             try:
                trainer_contract  =  course.trainers.get(trainer__user = user)
                course.trainers.remove(trainer_contract)
                if trainer_contract.trainer_contract_course_set.all().count() == 0 : 
                        trainer_contract.delete()
             except Exception as r:
                  print(r)
                  raise ValidationError({"message":"user is already trainee"})
             
          #change  trainee to trainer
          elif role.lower() == 'trainer':
              trainee_contract = course.trainees.filter(trainee__user = user)
              if trainee_contract:
                 trainer,_ = Trainer.objects.get_or_create(user = user)
                 trainer_contract,_ = Trainer_Contract.objects.get_or_create(trainer = trainer , company = course.company, employed =True)
                 course.trainers.add(trainer_contract)
                 course.save()
                 user.is_trainer = True
                 user.save()
              else:
                  raise ValidationError({"message":"the user is niether trainee nor trainer in this course add it first"})
          

          return Response({"message":f"The {user.username} he is {role} in course {course.name} now"})