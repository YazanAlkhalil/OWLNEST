# django
from django.http import Http404
# rest framerwork
from rest_framework import permissions
#  models
from ..models.Company import Company
from ..models.Course import Course
from ..models.Trainee_Contract import Trainee_Contract

class IsTrainee(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        return request.user.is_trainee

class IsCompanyTrainee(permissions.BasePermission):
    def has_permission(self, request, view): 
        company = Company.objects.get(id = view.kwargs["company_id"])
        if company.trainees.filter(trainee_contract__trainee__user=request.user, trainee_contract__employed=True).exists():
            return True
        raise Http404({'message': f'{request.user} Is Not Trainer In Company {company}'})

class IsCourseTrainee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        company_id = view.kwargs.get('company_id')
        course_id = view.kwargs.get('course_id')
        if isinstance(obj, Course):
            try:
                Trainee_Contract.objects.get(trainee=request.user.trainee, course=course_id, company__id=company_id, employed=True)
                return obj.trainees.filter(trainee=request.user.trainee).exists()
            except Trainee_Contract.DoesNotExist:
                raise Http404({'message': f'{request.user} Is Not A Trainee In Course {obj}'})