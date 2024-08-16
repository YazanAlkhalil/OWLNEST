from django.urls import path


#views  
from system.views.AddContentToUnit import AddContentToUnit
from system.views.TrainerRetrieveContentView import TrainerRetrieveContentView 
urlpatterns = [
   
    path(
        'trainer/company/<int:company_id>/courses/<int:course_id>/unit/<int:unit_id>/content/create', 
        AddContentToUnit.as_view(), 
        name='content-trainer-create'
    ),  
    path(
        'content/<int:id>', 
        TrainerRetrieveContentView.as_view(),  
    ), 
  
   
]