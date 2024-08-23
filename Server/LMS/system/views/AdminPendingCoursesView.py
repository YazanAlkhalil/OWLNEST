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
            if company.owner.user == self.request.user :
               owner = self.request.user.owner
               courses = [app.course for app in owner.ownerapprovment_set.all()]
               print(courses)
               return courses
            if hasattr(self.request.user,'admin') :
               admin = self.request.user.admin.admin_contract_set.get(company = company)
               print(admin.adminapprovment_set.all())
               courses = [app.course for app in admin.adminapprovment_set.all()]
               print(courses)
               return courses
            
          