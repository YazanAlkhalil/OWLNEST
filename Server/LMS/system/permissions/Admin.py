# django
from django.http import Http404
# rest framework
from rest_framework import permissions
# models
from system.models.Company import Company
from ..models.Course import Course
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
from ..models.Admin_Contract import Admin_Contract

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin

class IsCompanyAdmin(permissions.BasePermission):
    def has_permission(self, request, view): 
        company = Company.objects.get(id = view.kwargs["company_id"])
        if company.admins.filter(admin_contract__admin__user=request.user,admin_contract__employed=True).exists():
            return True
        raise Http404({'message': f'{request.user} Is Not The Admin For Company {company}'})

class IsCourseAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        company_id = view.kwargs.get('company_id')
        course_id = view.kwargs.get('course_id')
        if isinstance(obj, Course):
            try:
                Admin_Contract.objects.get(admin=request.user.admin, course=course_id, company__id=company_id, employed=True)
                return obj.admin_contract.admin == request.user.admin
            except Admin_Contract.DoesNotExist:
                raise Http404({'message': f'{request.user} Is Not The Admin For Course {obj}'})
        elif isinstance(obj, Unit) or isinstance(obj, Temp_Unit):
            try:
                Admin_Contract.objects.get(admin=request.user.admin, course=course_id, company__id=company_id, employed=True)
                return obj.course.admin_contract.admin == request.user.admin
            except Admin_Contract.DoesNotExist:
                raise Http404({'message': f'{request.user} Is Not The Admin For Course {obj.course}'})