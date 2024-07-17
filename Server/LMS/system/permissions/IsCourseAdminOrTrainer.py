from rest_framework import permissions

class IsCourseAdminOrTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        # Check if the user is the admin or a trainer of the course
        if request.user.is_admin:
            return obj.admin_contract.admin == request.user.admin
        # Check if the user is a trainer of the course
        if request.user.is_trainer:
            return obj.trainers.filter(trainer=request.user.trainer).exists()
        return False