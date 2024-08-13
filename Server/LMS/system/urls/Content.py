from django.urls import path
from ..views.Content import (
    ContentList, 
    ContentRetrieve, 
    ContentCreate, 
    ContentUpdate, 
    ContentDelete, 
    ContentRestore, 
    TempContentDelete
)

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
    #################
    #               #
    #    Create     #
    #               #
    #################
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/create', 
        ContentCreate.as_view(), 
        name='content-trainer-create'
    ),
    #################
    #               #
    #    Update     #
    #               #
    #################
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/update', 
        ContentUpdate.as_view(), 
        name='content-trainer-update'
    ),
    #################
    #               #
    #    Delete     #
    #               #
    #################
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/delete', 
        ContentDelete.as_view(), 
        name='content-trainer-delete'
    ),
    #################
    #               #
    #    Restore    #
    #               #
    #################
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/restore', 
        ContentRestore.as_view(), 
        name='content-trainer-restore'
    ),
    #########################
    #                       #
    #  Delete Unpublished   #
    #                       #
    #########################
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/<int:content_id>/not_published/delete', 
        TempContentDelete.as_view(), 
        name='content-trainer-not-published-delete'
    ),
]