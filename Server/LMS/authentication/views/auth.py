from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from authentication.serializers.userSerializer import UserSerializer,ResetPasswordEmailREquestSerializer,SetNewPasswordSerializer
from authentication.models import User
import re
from rest_framework import generics
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str ,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from authentication.authentication import createAccessToken,createRefreshToken,decodeAccessToken,decodeRefreshToken

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
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

        response = Response()

        response.set_cookie(key='accessToken',value=accessToken ,httponly=True,samesite='None',secure=True)
        response.set_cookie(key='refreshToken',value=refreshToken ,httponly=True,samesite='None',secure=True)
        request.session['refresh_token_used'] = False
        print(response)

        return response

class UserView(APIView):
    def get(self, request):
        if request.user:
            return Response(UserSerializer(request.user).data)
        raise AuthenticationFailed('unauthenticated')

class RefreshApiView(APIView):
    def post(self,request):
        refreshToken = request.COOKIES.get('refreshToken')
        userId = decodeRefreshToken(refreshToken)
        if userId is None:
            raise AuthenticationFailed('Invalid refresh token')
        
        if request.session.get('refresh_token_used', False):  
            response = Response({'error': 'Refresh token has already been used'})
            response.status_code = 403
            return response
        
        request.session['refresh_token_used'] = True 
        accessToken = createAccessToken(userId)
        response = Response({
            'accessToken': accessToken
        })
        response.delete_cookie('refreshToken')
        response.set_cookie(key='accessToken',value=accessToken ,httponly=True)
        return response


class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('accessToken')
        response.delete_cookie('refreshToken')
        response.data = {
            'message':'success'
        }
        return response

class ForgetPassword(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        if not re.match(r'^[^@]+@gmail\.com$', email):
            return Response({'message': 'Invalid email. Only Gmail addresses are allowed.'}, status=400)
        user = User.objects.filter(email=email).first()
        if user:
            user.set_password(password)
            user.save()
            return Response({'message':'success'})
        else:
            return Response({'message':'user not found'})

class DeleteUserView(APIView):
    def delete(self, request):
        pk = request.data['id']
        user = User.objects.filter(pk=pk).first()
        if user:
            user.delete()
            return Response({'message': 'User deleted successfully'})
        else:
            return Response({'message': 'User not found'}, status=404)
        

class RequestPasswordResetEmail(generics.GenericAPIView):
    
    serializer_class = ResetPasswordEmailREquestSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        email = request.data['email']
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb46 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request = request).domain
            relativeLink = reverse('password_reset_confirm',kwargs= {'uidb46':uidb46 , 'token':token})
            absurl = 'http://localhost:3000/newPassword'
            email_body = 'Hi' + user.username + 'use link below to reset your password \n'
            #data = {'email_body' : email_body , 'to_email':user.email , 'email_subject':'reset your password'}
            subject = "Join a company "
            message = 'Hi ' + user.username + ' use link below to reset your password \n'+absurl
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return Response({'success':'we have sent a link to reset your password'}, status = 200)


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
    serialaizer_class = SetNewPasswordSerializer
    def patch(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_excpetion = True)
        return Response({
            'success':True,
            'message':'password reset success',
        },
        status = 200)



