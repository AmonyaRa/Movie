from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from applications.account.serializers import RegisterUserSerializer

# Create your views here.

User = get_user_model()


class RegisterUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
