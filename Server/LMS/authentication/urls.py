from django.urls import path
from authentication.views.auth import RegisterView,LoginView,UserView,LogoutView,RefreshApiView
from authentication.views.otp import OTPVerificationView,VerifyOTPView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('refresh/',RefreshApiView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('send_otp/',OTPVerificationView.as_view()),
    path('verify_otp/', VerifyOTPView.as_view()),
]
