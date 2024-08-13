# django
from django.http import Http404
# rest framerwork
from rest_framework import permissions
#  models
from ..models.Company import Company
from ..models.Course import Course
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
from ..models.Trainer_Contract import Trainer_Contract

class IsTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        return request.user.is_trainer

class IsCompanyTrainer(permissions.BasePermission):
    def has_permission(self, request, view): 
        company = Company.objects.get(id = view.kwargs["company_id"])
        if company.trainers.filter(trainer_contract__trainer__user=request.user, trainer_contract__employed=True).exists():
            return True
        raise Http404({'message': f'{request.user} Is Not Trainer In Company {company}'})

class IsCourseTrainer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        company_id = view.kwargs.get('company_id')
        course_id = view.kwargs.get('course_id')
        if isinstance(obj, Course):
            try:
                Trainer_Contract.objects.get(trainer=request.user.trainer, trainer_contract_course__course=course_id, company__id=company_id, employed=True)
                return obj.trainers.filter(trainer=request.user.trainer).exists()
            except Trainer_Contract.DoesNotExist:   
                raise Http404({'message': f'{request.user} Is Not A Trainer In Course {obj}'})
        elif isinstance(obj, Unit) or isinstance(obj, Temp_Unit):
            try:
                Trainer_Contract.objects.get(trainer=request.user.trainer, trainer_contract_course__course=course_id, company__id=company_id, employed=True)
                return obj.course.trainers.filter(trainer=request.user.trainer).exists()
            except Trainer_Contract.DoesNotExist:
                raise Http404({'message': f'{request.user} Is Not A Trainer In Course {obj.course}'})