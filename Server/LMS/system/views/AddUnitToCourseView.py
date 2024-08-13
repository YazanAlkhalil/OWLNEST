#DRF
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.Course import Course

#serializer
from system.serializers.DraftUnitSerializer import DraftUnitSerializer

#django 
from django.shortcuts import get_object_or_404

class AddUnitToCourse(CreateAPIView):
      serializer_class = DraftUnitSerializer
      permission_classes = [IsAuthenticated]

      def post(self, request, *args, **kwargs):
          if not( "title" in request.data.keys()):
              raise ValidationError({"message":"Please Enter the unit title"}) 
          if not( "order" in request.data.keys()):
               raise ValidationError({"message":"Please Enter the unit order"}) 
          course = get_object_or_404(Course,id = kwargs["course_id"])
          data = {
               "title":request.data["title"],
               "order" :request.data["order"] }
          serialized_unit = DraftUnitSerializer(data =data )
          serialized_unit.is_valid(raise_exception=True)
          serialized_unit.save(course = course)
          return Response({"message":"The unit added successfully"},200)