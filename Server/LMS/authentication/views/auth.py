from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from rest_framework import generics
from rest_framework import status
from authentication.serializers.userSerializer import UserSerializer,ResetPasswordEmailREquestSerializer,SetNewPasswordSerializer
from authentication.models import User
import re
from datetime import datetime
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str ,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError

from authentication.authentication import createAccessToken,createRefreshToken,decodeAccessToken,decodeRefreshToken

class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            raise ValidationError('Email is required for registration.')

        existing_user = User.objects.filter(email=email).first()

        if existing_user and not existing_user.otp_verified:
            existing_user.delete()

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed('user not found')
        
        if user.otp_verified is False:
            raise AuthenticationFailed('user not verified')
        
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        accessToken = createAccessToken(user.id)
        refreshToken = createRefreshToken(user.id)

        user.last_login = datetime.now()
        user.save()

        response = Response()

        response.set_cookie(key='accessToken',value=accessToken ,httponly=True,samesite='None',secure=True, max_age=3600)
        response.set_cookie(key='refreshToken',value=refreshToken ,httponly=True,samesite='None',secure=True, max_age=3600*7*24)
        request.session['refresh_token_used'] = False
        print(response)

        return response

class UserView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            return Response(UserSerializer(user).data)
        raise AuthenticationFailed('unauthenticated')

class RefreshApiView(APIView):
    def post(self,request):
        Token = request.COOKIES.get('refreshToken')
        refresh_token = decodeRefreshToken(Token)
        #payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = refresh_token["user_id"]
        exp = refresh_token["exp"]
        if datetime.fromtimestamp(exp) < datetime.now():
            response = Response()
            response.set_cookie(key='accessToken',value="" ,httponly=True,samesite='None',secure=True, max_age=3600)
            response.set_cookie(key='refreshToken',value="" ,httponly=True,samesite='None',secure=True, max_age=3600*7*24)
            response.delete_cookie('accessToken')
            response.delete_cookie('refreshToken')

            response.data = {
                'message':'refresh token has expiered',
            }

            return response
        accessToken = createAccessToken(user_id)
        response = Response()
        response.set_cookie(key='accessToken',value=accessToken ,httponly=True,samesite='None',secure=True, max_age=3600)
        response.data = {
                'message':'success',
                'token':accessToken
        }

        return response
        
# class RefreshApiView(APIView):
#     def post(self,request):
#         refreshToken = request.COOKIES.get('refreshToken')
#         userId = decodeRefreshToken(refreshToken)
#         if userId is None:
#             raise AuthenticationFailed('Invalid refresh token')
        
#         if request.session.get('refresh_token_used', False):  
#             return Response({'error': 'Refresh token has already been used'},status= 403)
#         request.session['refresh_token_used'] = True 
#         response = Response()
#         response.delete_cookie('refreshToken')
#         response.set_cookie(key='accessToken', value=refreshToken, httponly=True)
#         return response


class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.set_cookie(key='accessToken',value="" ,httponly=True,samesite='None',secure=True, max_age=3600)
        response.set_cookie(key='refreshToken',value="" ,httponly=True,samesite='None',secure=True, max_age=3600*7*24)
        response.delete_cookie('accessToken')
        response.delete_cookie('refreshToken')
 
        response.data = {
            'message':'success'
        }
        return response


class DeleteUserView(APIView):
    def delete(self, request):
        pk = request.data['id']
        user = User.objects.filter(pk=pk).first()
        if user:
            user.delete()
            return Response({'message': 'User deleted successfully'})
        else:
            return Response({'message': 'User not found'}, status=404)
        

class EditProfielView(APIView):
    def patch(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            user = request.user
            user_data = request.data
            if 'old_password' in user_data:
                old_password = user_data['old_password']
                if not user.check_password(old_password):
                    return Response({'message': 'old password is not correct'}, status=400)
                new_password = user_data['new_password']
                user.set_password(new_password)  # <--- Use set_password to hash the new password
                user.save()
            serializer = UserSerializer(user, data=user_data, partial=True)
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'user not found'}, status=404)

class RequestPasswordResetEmail(generics.GenericAPIView):
    
    serializer_class = ResetPasswordEmailREquestSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        email = request.data['email']
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request = request).domain
            relativeLink = reverse('password_reset_confirm',kwargs= {'uidb64':uidb64 , 'token':token})
            absurl = 'http://localhost:3000/newPassword'+relativeLink
            email_body = 'Hi' + user.username + 'use link below to reset your password \n'
            #data = {'email_body' : email_body , 'to_email':user.email , 'email_subject':'reset your password'}
            subject = "Join a company "
            message = 'Hi ' + user.username + ' use link below to reset your password \n'+absurl
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return Response({'success':'we have sent a link to reset your password'}, status = 200)
        
        return Response({'message':'user not found'}, status = 400)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self,request,uidb64,token):
        try : 
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'error':'Token is not valid, please request a new one'}, status=401)
            return Response({'success':True, 'message':'Credentials valid', 'uidb64':uidb64 , 'token':token})
        
        except DjangoUnicodeDecodeError as identifier:
            return Response({'error':'Token is not valid, please request a new one'}, status=401)
        

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def patch(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        return Response({
            'success':True,
            'message':'password reset success',
        },
        status = 200)



