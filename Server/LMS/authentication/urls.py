from django.urls import path
from authentication.views.auth import RegisterView,LoginView,UserView,LogoutView,RefreshApiView,SetNewPasswordAPIView
from authentication.views.otp import OTPVerificationView,VerifyOTPView

from django.contrib.auth import views as auth_views
from authentication.views.auth import PasswordTokenCheckAPI,RequestPasswordResetEmail,EditProfielView



urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('refresh/',RefreshApiView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('send_otp/',OTPVerificationView.as_view()),
    path('verify_otp/', VerifyOTPView.as_view()),
    path('request_reset_email/',RequestPasswordResetEmail.as_view(),name='request_reset_email' ),
    path('password_reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',SetNewPasswordAPIView.as_view(),name='password_reset_complete'),
    path('edit_profile/',EditProfielView.as_view(),name='edit_profile'),
]
