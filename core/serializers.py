# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import password_validation

import re
from .models import Event, User

class CustomTokenObtainSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # self.username_field = "email"
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['message'] = "Loggedin Successful. Use the obtained access key as JWT token and refresh key to refresh jwt token"
        return data


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'full_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, data):
        if not (len(data['username']) == 7 and re.search(r'^(?!.*(.).*\1)[A-Za-z0-9]+$', data['username'])):
            raise serializers.ValidationError("Username must be 7 characters and all unique")
        if not (len(data['password']) >= 6 and re.search(r'^[A-Za-z0-9]+$', data['password'])):
            raise serializers.ValidationError("Password must be atleast 6 characters")
        if not(len(data['full_name']) >= 0 and re.search(r'^[^\s]+( [^\s]+)+$', data['full_name'])):
            raise serializers.ValidationError("Full Name must be as 'first_name last_name'")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password = validated_data['password'],
            email=validated_data['email'],
            full_name= validated_data['full_name'],
            first_name=validated_data['full_name'].split(" ")[0],
            last_name=validated_data['full_name'].split(" ")[1],
            is_active=True
            )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                'Your old password was entered incorrectly. Please enter it again.'
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': "The two password fields didn't match."})
        if not (len(data['new_password1']) >= 6 and re.search(r'^[A-Za-z0-9]+$', data['new_password1'])):
            raise serializers.ValidationError("Password must be atleast 6 characters")
        if not (len(data['new_password2']) >= 6 and re.search(r'^[A-Za-z0-9]+$', data['new_password2'])):
            raise serializers.ValidationError("Password must be atleast 6 characters")
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'mobile_number']


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = "__all__"
