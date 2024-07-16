from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from authentication.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str ,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','phone','birthday','gender','country']

        extra_kwargs = {
            'password' : {'write_only':True}
        }


    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ResetPasswordEmailREquestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=4)
    class Meta:
        fields = ['email']

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, write_only=True
    )
    uidb64 = serializers.CharField(
        min_length=1, write_only=True
    )
    token = serializers.CharField(
        min_length=1, write_only=True
    )

    class Meta:
        fields = ['password','uidb64','token']

    def validate(self,attrs):
        try:
            password = attrs.get('password')
            uidb64 = attrs.get('uidb64')
            token = attrs.get('token')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('the reset link is invalid ' ,401)

            user.set_password(password)
            user.save()

        except ValueError:
            raise AuthenticationFailed('Invalid uidb64 or token', 401)

        return super().validate(attrs)