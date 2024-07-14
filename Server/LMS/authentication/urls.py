from django.urls import path
from authentication.views.auth import RegisterView,LoginView,UserView,LogoutView,RefreshApiView,ForgetPassword,SetNewPasswordAPIView
from authentication.views.otp import OTPVerificationView,VerifyOTPView

from django.contrib.auth import views as auth_views
from authentication.views.auth import PasswordTokenCheckAPI,RequestPasswordResetEmail



urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('refresh/',RefreshApiView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('send_otp/',OTPVerificationView.as_view()),
    path('verify_otp/', VerifyOTPView.as_view()),
    path('forget_password/', ForgetPassword.as_view()),
    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name="authentication\templets\authentication\password_reset_email.html"),name="reset_password"),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="authentication\templets\authentication\password_reset_email.html"),name="password_reset_done"),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('request_reset_email/',RequestPasswordResetEmail.as_view(),name='request_reset_email' ),
    path('password_reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',SetNewPasswordAPIView.as_view(),name='password_reset_complete'),
]
