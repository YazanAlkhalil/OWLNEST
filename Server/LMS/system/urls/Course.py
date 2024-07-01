from django.urls import path
from ..views.Course import CompanyCourseListCreate, CompanyCourseRetrieveUpdateDestroy, CompanyCourseRetriveInfo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'company/<int:company_id>/courses/', 
        CompanyCourseListCreate.as_view(), 
        name='company-course-list-create'
    ),
    path(
        'company/<int:company_id>/courses/<int:course_id>/', 
        CompanyCourseRetrieveUpdateDestroy.as_view(), 
        name='company-course-detail'
    ),
    path(
        'company/<int:company_id>/courses/<int:course_id>/info',
        CompanyCourseRetriveInfo.as_view(),
        name='company-course-info'
    ),
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)