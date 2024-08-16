# rest framerwork
from rest_framework import permissions
#  models
from ..models.Company import Company
from ..models.Company_Planes import Company_Planes
from rest_framework.exceptions import ValidationError

class DoesHaveAPlane(permissions.BasePermission):
    def has_permission(self, request, view):
        company = Company.objects.get(id=view.kwargs['company_id'])
        company_planes = Company_Planes.objects.filter(company__id=company.id, is_active=True, is_full=False)
        if company_planes.__len__() > 0:
            for company_plane in company_planes:
                if company_plane.current_courses_number < company_plane.plane.courses_number:
                    return True
        raise ValidationError({'message': f'Company {company} Doesn\'t have an active plane, Purchase a new one'})