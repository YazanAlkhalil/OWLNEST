from django.urls import path
                    
#views 
from system.views.AddUnitToCourseView import AddUnitToCourse
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
        AddUnitToCourse.as_view(), 
        name='unit-trainer-create'
    ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/update', 
    #     UnitUpdate.as_view(), 
    #     name='unit-trainer-update'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/delete', 
    #     UnitDelete.as_view(), 
    #     name='unit-trainer-delete'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/restore', 
    #     UnitRestore.as_view(), 
    #     name='unit-trainer-restore'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/not_published/delete', 
    #     TempUnitDelete.as_view(), 
    #     name='unit-trainer-not-published-delete'
    # ),
]