from django.urls import path
                    
#views 
from system.views.AddUnitToCourseView import AddUnitToCourse
from system.views.DeleteDraftUnitView import DeleteDraftUnitView
urlpatterns = [ 
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/create', 
        AddUnitToCourse.as_view(), 
        name='unit-trainer-create'
    ),
    path(
      'unit/<id>',
      DeleteDraftUnitView.as_view()
    )  
]