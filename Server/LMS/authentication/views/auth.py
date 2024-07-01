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
        
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        

        accessToken = createAccessToken(user.id)
        refreshToken = createRefreshToken(user.id)


        response = Response()

        response.set_cookie(key='refreshToken',value=refreshToken ,httponly=True)
        response.data = {
            'token' : accessToken
        }

        return response


class UserView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) ==2:
            token = auth[1].decode('utf-8')
            id = decodeAccessToken(token)
            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)
        
        raise AuthenticationFailed('anauthenticated')

class RefreshApiView(APIView):
    def post(self,request):
        refreshToken = request.COOKIES.get('refreshToken')
        id = decodeRefreshToken(refreshToken)
        access_Token = createAccessToken(id)
        return Response({
            'token':access_Token
        })


class LogoutView(APIView):

    def post(self,request):

        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }

        return response