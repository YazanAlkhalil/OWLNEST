from django.urls import path
from ..views.Test import DeleteTest

urlpatterns = [
    ##############
    #   Delete   #
    ##############
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/tests/<int:test_id>/delete',
        DeleteTest.as_view(),
        name='test-delete'
    ),
]