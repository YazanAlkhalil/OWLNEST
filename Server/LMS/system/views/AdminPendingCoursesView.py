#DRF
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


#models 
from system.models.Company import Company


#serializer

from system.serializers.AdminCourseListSerializer import AdminCourseListSerializer

#django 
from django.shortcuts import get_object_or_404


class AdminPendingCoursesView(ListAPIView):
      serializer_class = AdminCourseListSerializer
      permission_classes = [IsAuthenticated]
      def get_queryset(self):
            company = get_object_or_404(Company,id = self.kwargs["company_id"])
            if hasattr(self.request.user,'admin') :
               admin = self.request.user.admin.admin_contract_set.get(company = company)
               courses = [app.course for app in admin.adminapprovment_set.all()]
               return courses
            
          