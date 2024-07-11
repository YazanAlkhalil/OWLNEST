from django.urls import path
from ..views.Course import CompanyCourseList, CompanyCourseCreate, CompanyCourseRetrieve, CompanyCourseUpdate, CompanyCourseDelete, CompanyCourseRetriveInfo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'admin/company/<int:company_id>/courses/', 
        CompanyCourseList.as_view(), 
        name='company-course-admin-list'
    ),
    path(
        'trainer/company/<int:company_id>/courses/', 
        CompanyCourseList.as_view(), 
        name='company-course-trainer-list'
    ),
    path(
        'trainee/company/<int:company_id>/courses/', 
        CompanyCourseList.as_view(), 
        name='company-course-trainee-list'
    ),
    path(
        'admin/company/<int:company_id>/courses/', 
        CompanyCourseCreate.as_view(), 
        name='company-course-admin-create'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>', 
        CompanyCourseRetrieve.as_view(), 
        name='company-course-admin-retrive'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>', 
        CompanyCourseRetrieve.as_view(), 
        name='company-course-trainer-retrive'
    ),
    path(
        'trainee/company/<int:company_id>/courses/<int:course_id>', 
        CompanyCourseRetrieve.as_view(), 
        name='company-course-trainee-retrive'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>', 
        CompanyCourseUpdate.as_view(), 
        name='company-course-admin-update'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>', 
        CompanyCourseUpdate.as_view(), 
        name='company-course-trainer-update'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>',
        CompanyCourseDelete.as_view(),
        name='company-course-admin-delete'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/info',
        CompanyCourseRetriveInfo.as_view(),
        name='company-course-admin-info'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/info',
        CompanyCourseRetriveInfo.as_view(),
        name='company-course-trainer-info'
    ),
    path(
        'trainee/company/<int:company_id>/courses/<int:course_id>/info',
        CompanyCourseRetriveInfo.as_view(),
        name='company-course-trainee-info'
    ),
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)