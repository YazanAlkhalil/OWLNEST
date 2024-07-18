from django.urls import path
from ..views.Unit import UnitList, UnitRetrieve, UnitCreate, UnitUpdate, UnitDelete

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
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/create', 
        UnitCreate.as_view(), 
        name='unit-trainer-create'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/update', 
        UnitUpdate.as_view(), 
        name='unit-trainer-update'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/delete', 
        UnitDelete.as_view(), 
        name='unit-trainer-delete'
    ),
]