import re
from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework_simplejwt import views as jwt_views 

from .serializers import (
    RegisterSerializer, UserSerializer, EventSerializer,
    CustomTokenObtainSerializer, ChangePasswordSerializer
)
from .models import Event, User

# Create your views here.

class CustomTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer

    def post(self, request):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,request.data['username'])):
            request.data['username'] = User.objects.get(email=request.data['username']).username
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().post(request)

class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": request.data,
            "message": "User Created Successfully.  Now Login to get your token",
        })


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()        
        return Response({'message': "Password changed Successfully"})


class UserListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ) 

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ) 

    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, ) 

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ) 

    queryset = Event.objects.all()
    serializer_class = EventSerializer