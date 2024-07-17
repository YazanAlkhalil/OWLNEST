from rest_framework import permissions

class IsCourseTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        # Check if the user is a trainer of the course
        if request.user.is_trainer:
            return obj.trainers.filter(trainer=request.user.trainer).exists()
        return False