# django
from django.http import Http404
# rest framework
from rest_framework import permissions
# models
from system.models.Company import Company
from ..models.Course import Course
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        return request.user.is_owner

class IsCompanyOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        company = Company.objects.get(id = view.kwargs['company_id'])
        if company.owner.user == request.user:
            return True
        raise Http404({'message': f'{request.user} Is Not The Owner For Company {company}'})

class isCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Course):
            if obj.company.owner == request.user.owner:
                return True    
            raise Http404({'message': f'{request.user} Is Not The Owner For Course {obj}'})
        elif isinstance(obj, Unit) or isinstance(obj, Temp_Unit):
            if obj.company.owner == request.user.owner:
                return True
            raise Http404({'message': f'{request.user} Is Not The Owner For Course {obj.course}'})