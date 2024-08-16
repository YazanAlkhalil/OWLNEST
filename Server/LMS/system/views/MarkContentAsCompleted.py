#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#models  
from system.models.Enrollment import Enrollment
from system.models.Content import Content
from system.models.Finished_Content import Finished_Content
#serializers 
from system.serializers.MarkContentSerializer import MarkContentSerializer
from rest_framework.permissions import IsAuthenticated
#django
from django.shortcuts import get_object_or_404
from django.utils import timezone


class MarkContentView(APIView):
      serializer_class = MarkContentSerializer
      permission_classes = [IsAuthenticated]
      
      def post(self, request, *args, **kwargs): 
          enrollment =  get_object_or_404(Enrollment,trainee_contract__trainee__user = request.user , course__id = kwargs["id"])
          content = get_object_or_404(Content,id =kwargs["content_id"])
          if enrollment.course != content.unit.course :
               return Response({"message":"you can't mark content if you are not enroll in this course"},status.HTTP_400_BAD_REQUEST)
           
          if content.id in [content.content.id for content in enrollment.finished_content_set.all()]:
               return Response({"message":"you already mark it as completed"})
          
          marked_content = Finished_Content.objects.create(enrollment= enrollment , content = content)

          
            
          if  enrollment.progress == 100 and not (enrollment.completed):
               sum = 0.0
               passed = Tr
               for grade in enrollment.grade_set.all():
                   sum +=grade.score 
                   enrollment.completed = True
                   enrollment.completed_at = timezone.now()
                   enrollment.save() 
                   #generate pdf

                   return Response({"message":"passed"}, 200)
           
          
          return Response({"message":"next"},status.HTTP_200_OK)
