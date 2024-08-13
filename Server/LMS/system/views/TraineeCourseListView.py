#DRF
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated


#models 
from system.models.Course  import Course  
from system.models.Trainee_Contract import Trainee_Contract



#serializer 
from system.serializers.TraineeCourseListSerializer import TraineeCourseListSerializer  
 
 

class TraineeCourseListView(generics.ListAPIView):
      serializer_class = TraineeCourseListSerializer
      permission_classes = [IsAuthenticated]

      def get_queryset(self):
          user = self.request.user
          company_id = self.kwargs.get('company_id') 
          trainee_contracts = Trainee_Contract.objects.filter(trainee__user=user, employed=True, company_id=company_id)
          courses = Course.objects.filter(
              company__id=company_id,
              trainees__in=trainee_contracts,
              published = True
          ).distinct()
          return courses  