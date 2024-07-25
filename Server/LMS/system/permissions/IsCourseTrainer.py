from rest_framework import permissions
from ..models.Course import Course
from ..models.Unit import Unit
from ..models.Temp_unit import Temp_Unit
class IsCourseTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Course):
            # Check if the user is a trainer of the course
            if request.user.is_trainer:
                return obj.trainers.filter(trainer=request.user.trainer).exists()
            return False
        elif isinstance(obj, Unit) or isinstance(obj, Temp_Unit):
            # Check if the user is a trainer of the course
            if request.user.is_trainer:
                return obj.course.trainers.filter(trainer=request.user.trainer).exists()
            return False
        return False