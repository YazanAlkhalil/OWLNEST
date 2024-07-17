from django.urls import path
from system.views.CreateCompany import CreateCompanyView,CompaniesView,DeleteOwnerView,DeleteCompanyView
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
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)