from django.urls import path
from system.views.CreateCompany import CreateCompanyView,CompaniesView,DeleteOwnerView,DeleteCompanyView,UserCompanyView,EditCompanyView,CompanyView
from system.views.AddUser import AddUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_company/', 
        CreateCompanyView.as_view(), 
        name='create_company'),

    path('delete_owner/', 
        DeleteOwnerView.as_view(), 
        name='delete_owner'),

    path('delete_company/', 
        DeleteCompanyView.as_view(), 
        name='delete_company'),

    path('add_user/', 
        AddUser.as_view(), 
        name='add_user'),

    path('get_companies/',
        CompaniesView.as_view(),
        name='get_companies'),

    path('company/<int:company_id>/roles/',
        UserCompanyView.as_view(),
        name='company_roles'),
    
    path('edit_company/',
        EditCompanyView.as_view(),
        name='edit_company'),
    
    path('company/',
        CompanyView.as_view(),
        name='ompany'),
]
