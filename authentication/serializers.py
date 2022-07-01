
import email
from .models import User
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=225, min_length=6)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password': 
            {'write_only': True,
            'required': True}
        }



    def create(self,  validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length= 225)

    class Meta:
        model = User
        fields = [
            'token'
        ]


class LoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length= 225)
    password= serializers.CharField(max_length= 225, write_only =True)
    username= serializers.CharField(max_length= 225, read_only=True)
    tokens= serializers.CharField(max_length= 225, read_only =True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'tokens'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email = email, password = password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.is_active:
            raise AuthenticationFailed('Account Inactive, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email not activated yet')
       

        return{
            'email' : user.email,
            'username': user.username,
            'tokens': user.tokens,
        }
        
        return super().validate(attrs)