from rest_framework.permissions import BasePermission
from ..models.Admin_Contract import Admin_Contract
from ..models.Course import Course

class IsOwnerOrAdminForCourse(BasePermission):
    def has_permission(self, request, view):
        # Get the course ID from the URL parameters
        course_id = view.kwargs.get('course_id')
        if request.user.is_admin:
            return Admin_Contract.objects.filter(admin=request.user.admin, course=course_id).exists()
        elif request.user.is_owner:
            course = Course.objects.filter(id=course_id)
            return course.owner.user == request.user
        else:
            return False