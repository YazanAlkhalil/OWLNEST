from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from authentication.serializers.userSerializer import UserSerializer
from authentication.models import User

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

        response.set_cookie(key='accessToken',value=accessToken ,httponly=True)
        response.set_cookie(key='refreshToken',value=refreshToken ,httponly=True)

        return response

class UserView(APIView):
    def get(self, request):
        accessToken = request.COOKIES.get('accessToken')
        if accessToken:
            id = decodeAccessToken(accessToken)
            user = User.objects.filter(pk=id).first()
            return Response(UserSerializer(user).data)
        raise AuthenticationFailed('unauthenticated')

class RefreshApiView(APIView):
    def post(self,request):
        refreshToken = request.COOKIES.get('refreshToken')
        return Response({
            'accessToken':refreshToken
        })


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