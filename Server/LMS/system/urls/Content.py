from django.urls import path


#views  
from system.views.AddContentToUnit import AddContentToUnit
urlpatterns = [
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content',
    #     ContentList.as_view(),
    #     name='content-admin-list'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content',
    #     ContentList.as_view(),
    #     name='content-trainer-list'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>',
    #     ContentRetrieve.as_view(),
    #     name='content-admin-retrive'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>',
    #     ContentRetrieve.as_view(),
    #     name='content-trainer-retrive'
    # ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/create', 
        AddContentToUnit.as_view(), 
        name='content-trainer-create'
    ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/update', 
    #     ContentUpdate.as_view(), 
    #     name='content-trainer-update'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/delete', 
    #     ContentDelete.as_view(), 
    #     name='content-trainer-delete'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/restore', 
    #     ContentRestore.as_view(), 
    #     name='content-trainer-restore'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/not_published/delete', 
    #     TempContentDelete.as_view(), 
    #     name='content-trainer-not-published-delete'
    # ),
]