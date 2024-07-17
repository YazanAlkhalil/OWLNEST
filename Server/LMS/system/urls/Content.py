from django.urls import path
from ..views.Content import ContentCreate

urlpatterns = [
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/unit',
    #     UnitList.as_view(),
    #     name='unit-admin-list'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit',
    #     UnitList.as_view(),
    #     name='unit-trainer-list'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>',
    #     UnitRetrieve.as_view(),
    #     name='unit-admin-retrive'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>',
    #     UnitRetrieve.as_view(),
    #     name='unit-trainer-retrive'
    # ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content', 
        ContentCreate.as_view(), 
        name='content-trainer-create'
    ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>', 
    #     UnitUpdate.as_view(), 
    #     name='unit-trainer-update'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>', 
    #     UnitDelete.as_view(), 
    #     name='unit-trainer-delete'
    # ),
]