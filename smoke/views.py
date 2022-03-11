from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .permissions import AnonPermissionOnly
from .serializers import RegisterSerializers
from rest_framework import generics


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializers

