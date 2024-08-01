#DRF
from rest_framework import response
from rest_framework import status
from rest_framework import generics
#models
from system.models.Company import Company
from system.models.Course import Course

#serializer
from system.serializers.AdminCourseListSerializer import AdminCourseListSerializer


#permissions
from system.permissions.IsCourseAdminOrOwner import IsCourseAdminOrOwner

class AdminCourseList(generics.ListAPIView):
      serializer_class = AdminCourseListSerializer 
      permission_classes = [IsCourseAdminOrOwner]

      def get_queryset(self):
            return Course.objects.filter(company__id = self.kwargs["company_id"], admin_contract__admin__user = self.request.user)