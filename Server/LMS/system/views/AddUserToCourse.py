#DRF
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#system models 
from system.models.Course import Course
from system.models.Trainee_Contract import Trainee_Contract
from system.models.Trainer_Contract_Course import Trainer_Contract_Course
from system.models.Enrollment import Enrollment
from system.models.Trainer_Contract import Trainer_Contract 
from authentication.models.User import User
from system.models.Trainee import Trainee
from system.models.Trainer import Trainer
from system.models.Notification import Notification
#serializer
from system.serializers.AddUserToCourseSerializer import (AddTraineeToCourseSerializer)
from system.serializers.NotificationSerializer import NotificationSerializer
#django 
from django.shortcuts import get_object_or_404

#permissions
from system.permissions.IsAdminCourse import IsAdminCourse

#channels  
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#utils 
from system.utils import send_notification
'''
to create a trainee:
1) get trainee or craete it
2) get trainee_contract or create it
3) add trainee_contract to course (create Enrollment object)

to create a trainer :
1) get trainer or create it
2) get trainer_contract or create it
3) add trainer_contract ot course (create Trainer_Contract_Course object)
4) add trainer as trainee (using reusable chunk of code to add trainer as trainee)

'''
class AddUserToCourse(CreateAPIView):
      permission_classes = [IsAuthenticated,IsAdminCourse]
      serializer_class = AddTraineeToCourseSerializer
      
      def post(self, request, *args, **kwargs):
          course = get_object_or_404(Course,id = kwargs["id"])
          user = get_object_or_404(User, email = request.data['email']) 
          trainee , _ = Trainee.objects.get_or_create(user = user)
          trainee_contract , _ = Trainee_Contract.objects.get_or_create(trainee = trainee , company = course.company, employed =True)
          if not course.trainees.filter(id=trainee_contract.id).exists():
                course.trainees.add(trainee_contract)
                course.save()
          trainee.user.is_trainee = True
          trainee.user.save()

           
          message = f"Hello {user.username}, you have been successfully enrolled in the course '{course.name}' by admin {request.user.username}. Welcome aboard!"
          send_notification(request.user,user,message,course.company)
          if request.data["role"].lower() == 'trainer':
                trainer,_ = Trainer.objects.get_or_create(user = user)
                trainer_contract , _ = Trainer_Contract.objects.get_or_create(trainer = trainer , company = course.company, employed =True)
                if not course.trainers.filter(id=trainer_contract.id).exists():
                    course.trainers.add(trainer_contract)
                    course.save()#send notify for the trainee
                trainer.user.is_trainer = True
                trainer.user.save()
                 
                message = f"Hello {user.username}, you have been assigned as the Trainer for the course '{course.name}' by admin {request.user.username}. Congratulations and best of luck!"
                send_notification(request.user,user,message,course.company)
          return Response({"message":"the "+request.data["role"] +" " + user.username+" added to the course"} , status.HTTP_201_CREATED)