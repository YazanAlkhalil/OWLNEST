from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 


#views 
from system.views.AdminCourseListView import AdminCourseListView
from system.views.TraineeCourseListView import TraineeCourseListView
from system.views.TrainerCourseListView import TrainerCourseListView
from system.views.AdminCreateCourseView import AdminCreateCourseView
from system.views.TrainerInProgressCourseListView import TrainerInProgressCourseListView
from system.views.TrainerInProgressCourseDetailsView import TrainerInProgressCourseDetailsView
from system.views.ReorderCourseView import ReorderCourseView
from system.views.AddSkillToCourse import AddSkillToCourse
from system.views.AddAdditionalResourcesToCourse import AddAdditionalResourcesToCourse
from system.views.CourseSubmitView import CourseSubmitView
from system.views.AdminPendingCoursesView import AdminPendingCoursesView
from system.views.DisapprovmentView import DisapprovmentView
from system.views.AdminApprovmentView import AdminApprovmentView
from system.views.TraineeCourseDetailsView import TraineeCourseDetailsView



urlpatterns = [
    path(
        'admin/company/<int:company_id>/courses', 
        AdminCourseListView.as_view(), 
        name='company-course-admin-list'
    ),
    path(
        'trainer/company/<int:company_id>/courses', 
        TrainerCourseListView.as_view(), 
        name='company-course-trainer-list'
    ),
    path(
        'trainee/company/<int:company_id>/courses', 
        TraineeCourseListView.as_view(), 
        name='company-course-trainer-list'
    ),
      path(
        'trainer/company/<int:company_id>/course/<course_id>/reorder', 
        ReorderCourseView.as_view(), 
        name='company-course-trainer-list'
    ),
    
    path(
        'admin/company/<int:company_id>/pending_courses', 
        AdminPendingCoursesView.as_view(), 
        name='company-pending-course-admin-list'
    ),
     
    path(
        'trainer/company/<int:company_id>/progress_courses', 
        TrainerInProgressCourseListView.as_view(),  
    ),
      path(
        'trainer/company/<int:company_id>/progress_courses/<int:course_id>', 
        TrainerInProgressCourseDetailsView.as_view(),  
    ),
      path(
        'trainer/company/<int:company_id>/courses/<int:course_id>', 
        TrainerInProgressCourseDetailsView.as_view(),  
    ),
    path(
        'admin/company/<int:company_id>/courses/create', 
        AdminCreateCourseView.as_view(),  
    ),
    path(
        'course/<id>/skills', 
        AddSkillToCourse.as_view(),  
    ),
      path(
        'course/<id>/additional-resources', 
        AddAdditionalResourcesToCourse.as_view(),  
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/publish', 
        CourseSubmitView.as_view(), 
        name='company-course-trainer-publish'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/approve', 
        AdminApprovmentView.as_view(), 
        name='company-course-admin-approve'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/disapprove', 
        DisapprovmentView.as_view(), 
        name='company-course-admin-disapprove'
    ),
    path(
        'trainee/courses/<course_id>',
        TrainerInProgressCourseDetailsView.as_view()
    )
   
     
   
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)