#DRF 
from rest_framework.generics import RetrieveUpdateDestroyAPIView

#models 
from system.models.Course import Course 

#serializers 
from system.serializers.EditCourseInformationSerializer import EditCourseInformationSerializer


class EditDestroyCourseView(RetrieveUpdateDestroyAPIView):
      serializer_class = EditCourseInformationSerializer
      queryset = Course.objects.all()