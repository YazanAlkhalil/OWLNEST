from django.urls import path
from system.views.CreateCompany import CreateCompanyView,DeleteOwnerView,DeleteCompanyView
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
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)