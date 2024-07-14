from django.urls import path
from ..views.Unit import UnitList, UnitRetrieve, UnitCreate

urlpatterns = [
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/unit',
        UnitList.as_view(),
        name='unit-admin-list'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit',
        UnitList.as_view(),
        name='unit-admin-list'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>',
        UnitRetrieve.as_view(),
        name='unit-admin-retrive'
    ),
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>',
        UnitRetrieve.as_view(),
        name='temp-unit-admin-approve'
    ),
    path(
        'admin/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/temp_unit/<int:temp_unit_id>/approve',
        UnitCreate.as_view(),
        name='temp-unit-admin-approve'
    ),
]