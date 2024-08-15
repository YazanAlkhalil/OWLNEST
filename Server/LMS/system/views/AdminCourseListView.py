#DRF
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated


#models 
from system.models.Course  import Course  



#serializer
from system.serializers.AdminCourseListSerializer import AdminCourseListSerializer 
from system.permissions.IsAdmin import IsAdminInCompanyOrOwner

class AdminCourseListView(generics.ListAPIView):
      serializer_class = AdminCourseListSerializer
      permission_classes = [IsAuthenticated,IsAdminInCompanyOrOwner]
      def get_queryset(self): 
          return Course.objects.filter(company__id = self.kwargs["company_id"])

 