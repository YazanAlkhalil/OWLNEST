from rest_framework import permissions
from ..models.Course import Course
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
from ..models.Trainer_Contract import Trainer_Contract
class IsCourseAdminOrTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        company_id = view.kwargs.get('company_id')
        course_id = view.kwargs.get('course_id')
        if isinstance(obj, Course):
            # Check if the user is the admin or a trainer of the course
            if request.user.is_admin:
                if obj.admin_contract.employed:
                    return obj.admin_contract.admin == request.user.admin
            # Check if the user is a trainer of the course
            if request.user.is_trainer:
                if Trainer_Contract.objects.get(trainer=request.user.trainer, trainer_contract_course__course=course_id, company__id=company_id).employed:
                    return obj.trainers.filter(trainer=request.user.trainer).exists()
            return False
        elif isinstance(obj, Unit) or isinstance(obj, Temp_Unit):
            # Check if the user is the admin or a trainer of the course
            if request.user.is_admin:
                if obj.course.admin_contract.employed:
                    return obj.course.admin_contract.admin == request.user.admin
            # Check if the user is a trainer of the course
            if request.user.is_trainer:
                if Trainer_Contract.objects.get(trainer=request.user.trainer, trainer_contract_course__course=course_id, company__id=company_id).employed:
                    return obj.course.trainers.filter(trainer=request.user.trainer).exists()
            return False
        return False