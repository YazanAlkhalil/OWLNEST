# django
from django.http import Http404
# rest framework
from rest_framework import permissions
# models
from ..models.Company import Company
from ..models.Course import Course
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
from ..models.Admin_Contract import Admin_Contract

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin or request.user.is_owner

class IsCompanyOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        company = Company.objects.get(id=view.kwargs["company_id"])
        if (
            company.admins.filter(admin_contract__admin__user=request.user, admin_contract__employed=True).exists() 
            or 
            company.owner.user == request.user
        ):
            return True
        raise Http404({'message': f'{request.user} Is Not The Admin/Owner For Company {company}'})

class IsCourseOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        company_id = view.kwargs.get('company_id')
        course_id = view.kwargs.get('course_id')
        if isinstance(obj, Course):
            if request.user.is_admin:
                try:
                    Admin_Contract.objects.get(admin=request.user.admin, course=course_id, company__id=company_id, employed=True)
                    return obj.admin_contract.admin == request.user.admin
                except Admin_Contract.DoesNotExist:
                    raise Http404({'message': f'{request.user} Is Not The Admin For Course {obj}'})
            elif request.user.is_owner:
                if obj.company.owner == request.user.owner:
                    return True
                raise Http404({'message': f'{request.user} Is Not The Owner For Course {obj}'})
        elif isinstance(obj, Unit) or isinstance(obj, Temp_Unit):
            if request.user.is_admin:            
                try:
                    Admin_Contract.objects.get(admin=request.user.admin, course=course_id, company__id=company_id, employed=True)
                    return obj.course.admin_contract.admin == request.user.admin
                except Admin_Contract.DoesNotExist:
                    raise Http404({'message': f'{request.user} Is Not The Admin For Course {obj.course}'})
            elif request.user.is_owner:
                if obj.course.company.owner == request.user.owner:
                    return True
                raise Http404({'message': f'{request.user} Is Not The Owner For Course {obj.course}'})