from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 

from .serializers import RegisterSerializer, UserSerializer, EventSerializer
from .models import Event

# Create your views here.

# class RegisterApiView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args,  **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user,    context=self.get_serializer_context()).data,
#             "message": "User Created Successfully.  Now perform Login to get your token",
#         })


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