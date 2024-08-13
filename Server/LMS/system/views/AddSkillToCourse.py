#DRF
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.Course import Course

#serializer
from system.serializers.DraftSkillSerializer import DraftSkillSerializer

#django 
from django.shortcuts import get_object_or_404

class AddSkillToCourse(ListCreateAPIView):
      serializer_class = DraftSkillSerializer
      permission_classes = [IsAuthenticated]
      def get_queryset(self): 
           return get_object_or_404(Course ,id= self.kwargs["id"]).draftskill_set.all() 

      def post(self, request, *args, **kwargs):
          if not( "skill" in request.data.keys()):
              raise ValidationError({"message":"Please Enter the skill"}) 
          if not( "rate" in request.data.keys()):
               raise ValidationError({"message":"Please Enter the skill rate"}) 
          course =get_object_or_404(Course,id =  kwargs["id"])
          skill_data = {
               "skill":request.data.get('skill'),
               "rate":request.data.get('rate')
          }

          serialized_skill = DraftSkillSerializer(data = skill_data)
          serialized_skill.is_valid(raise_exception=True)
          serialized_skill.save(course = course)


          return Response({"message":"skill added to the course"})