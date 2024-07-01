import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from authentication.serializers.userSerializer import UserSerializer
from authentication.models import User
from django.core.mail import send_mail
from django.conf import settings

class OTPVerificationView(APIView):
    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        otp = str(random.randint(100000, 999999))  
        user.otp = otp
        user.save()

        subject = "Your One-Time Password (OTP)"
        message = f"Your OTP is: {otp}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return Response({'message': 'OTP sent successfully'})

class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data['email']
        otp = request.data['otp']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        if user.otp != otp:
            raise AuthenticationFailed('invalid OTP')

        user.otp_verified = True
        user.save()

        return Response({'message': 'OTP verified successfully'})