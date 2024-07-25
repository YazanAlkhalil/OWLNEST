from django.urls import path
from system.views.CreateCompany import CreateCompanyView,GetCompanyData,CompaniesView,DeleteOwnerView,DeleteCompanyView,UserCompanyView,EditCompanyView,CompanyView,CompanyUsers
from system.views.AddUser import AddUser
from system.views.DeleteUsers import DeleteUser,DeleteAdmin,AddAdmin
from system.views.Planes import GetPlanes,BuyPlane
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_company/', 
        CreateCompanyView.as_view(), 
        name='create_company'),
    
    path('get_company_data/', 
        GetCompanyData.as_view(), 
        name='get_company_data'),

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
        name='company'),
    
    path('company_users/<int:company_id>/',
        CompanyUsers.as_view(),
        name='company_users'),
    
    path('delete_user/<int:user_id>/',
        DeleteUser.as_view(),
        name='delete_user'),
    
    path('delete_admin/<int:user_id>/',
        DeleteAdmin.as_view(),
        name='delete_admin'),
    
    path('add_admin/<int:user_id>/',
        AddAdmin.as_view(),
        name='add_admin'),

    # path('planes/',
    #     GetPlanes.as_view(),
    #     name='planes'),

    # path('buyPlane/',
    #     BuyPlane.as_view(),
    #     name='buyPlane'),
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)