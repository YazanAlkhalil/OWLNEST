#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#models  
from system.models.Enrollment import Enrollment
from system.models.Content import Content
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
          data = {
               'enrollment':enrollment.id,
               'content':content.id 
          }
          serialized_data = MarkContentSerializer(data = data)
          serialized_data.is_valid(raise_exception= True)
          serialized_data.save()
          print("PROGRESS",enrollment.progress)
          #return appropriate response if the enrollment passed 
          if  enrollment.progress == 100 and not (enrollment.completed):
               sum = 0.0
               for grade in enrollment.grade_set.all():
                   sum +=grade.score
               grades_number =  (enrollment.grade_set.all().count())
               if grades_number > 0 and sum /grades_number >= 60 : 
                   enrollment.completed = True
                   enrollment.completed_at = timezone.now()
                   enrollment.save()
                   #generate pdf

                   return Response({"message":"passed"}, 200)
          
               return Response({"message":"course completed"}, 200)
          

          
          return Response({"message":"the content marked as complete"},status.HTTP_200_OK)
