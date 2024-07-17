from rest_framework import permissions

class IsCourseAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        # Check if the user is the admin or a trainer of the course
        if request.user.is_admin:
            return obj.course.admin_contract.admin == request.user.admin
        return False