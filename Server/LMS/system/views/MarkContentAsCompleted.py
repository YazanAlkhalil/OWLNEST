#DRF 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#models  
from system.models.Enrollment import Enrollment
from system.models.Content import Content
from system.models.Finished_Content import Finished_Content
from system.models.Grade import Grade
#serializers 
from system.serializers.MarkContentSerializer import MarkContentSerializer
from rest_framework.permissions import IsAuthenticated
#django
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db import transaction 

class MarkContentView(APIView):
      serializer_class = MarkContentSerializer
      permission_classes = [IsAuthenticated]
      def get_progress(self,enrollment):
            total_contents = Content.objects.filter(unit__course=enrollment.course).count()
            finished_contents = Finished_Content.objects.filter(enrollment=enrollment).count()
            submitted_tests = Grade.objects.filter(enrollment=enrollment,score__gte = 60).count()
            
            
            #progress
            if total_contents > 0:
              total_finished = finished_contents + submitted_tests 
              return (total_finished / total_contents) * 100
            return 0


      def post(self, request, *args, **kwargs):
        enrollment = get_object_or_404(Enrollment, trainee_contract__trainee__user=request.user, course__id=kwargs["id"])
        content = get_object_or_404(Content, id=kwargs["content_id"])
        
        if enrollment.course != content.unit.course:
            return Response({"message": "You can't mark content if you are not enrolled in this course"}, status=status.HTTP_400_BAD_REQUEST)
        
        if content.id in [finished_content.content.id for finished_content in enrollment.finished_content_set.all()]:
            return Response({"message": "You already marked it as completed"}, status=200)
        
        # Mark the content as finished
        Finished_Content.objects.create(enrollment=enrollment, content=content)
        
        # Update progress
        enrollment.progress = self.get_progress(enrollment)
        enrollment.save(update_fields=['progress'])  # Explicitly save the progress field
        
        if enrollment.progress == 100 and not enrollment.completed:
            passed = all(grade.score >= 60 for grade in enrollment.grade_set.all())
            
            if passed:
                enrollment.completed = True
                enrollment.completed_at = timezone.now()
                enrollment.save(update_fields=['completed', 'completed_at'])  # Save the completion status
        
                return Response({"status": "passed"}, status=status.HTTP_200_OK)
        
        return Response({"message": "Completed"}, status=status.HTTP_200_OK)

