from rest_framework import generics
from ..models.Course import Course
from ..models.Company import Company
from ..models.Admin_Contract import Admin_Contract
from ..serializers.Course import Course_Serializer

# POST: api/company/:company-id/courses
# GET : api/company/:company-id/courses
class CompanyCourseListCreate(generics.ListCreateAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # retrive the courses passed on the company id
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Course.objects.filter(company=company_id)
    # when listing the courses set the view_type as list, otherwise set it as detail
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'list' if self.request.method == 'GET' else 'detail'
        return context
    # save the created company info
    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        company = Company.objects.get(id=company_id)
        admin_contract_id = self.request.data.get('admin_contract')
        admin_contract = Admin_Contract.objects.get(id=admin_contract_id)
        serializer.save(company=company, admin_contract=admin_contract)

# GET   : api/company/:company-id/courses/course-id
# PUT   : api/company/:company-id/courses/course-id
# PATCH : api/company/:company-id/courses/course-id
# DELETE: api/company/:company-id/courses/course-id
class CompanyCourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # retrive the courses passed on the course id
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Course.objects.get(id=course_id)
    # set the view_type to detail (for sending most of the fields all but the description and additional_resources)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'detail'
        return context

class CompanyCourseRetriveInfo(generics.RetrieveAPIView):
    # set the serializer class
    serializer_class = Course_Serializer
    # retrive the courses passed on the course id
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Course.objects.get(id=course_id)
    # set the view_type to info (for sending all of the fields)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_type'] = 'info'
        return context