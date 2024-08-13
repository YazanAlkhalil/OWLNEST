#DRF
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated


#models 
from system.models.Course  import Course  
from system.models.Trainer_Contract import Trainer_Contract



#serializer 
from system.serializers.TrainerCourseListSerializer import TrainerCourseListSerializer  
 

class TrainerInProgressCourseListView(generics.ListAPIView):
      serializer_class = TrainerCourseListSerializer
      permission_classes = [IsAuthenticated]

      def get_queryset(self):
        user = self.request.user
        company_id = self.kwargs.get('company_id')
        trainer_contracts = Trainer_Contract.objects.filter(trainer__user=user, employed=True, company_id=company_id)
        courses = Course.objects.filter(
            company_id=company_id,
            trainers__in=trainer_contracts,
            published=False
        ).distinct()

        return courses