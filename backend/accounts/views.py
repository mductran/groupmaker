from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout


class LoginView(APIView):
    def post(self, request, format=None):
        pass

class LogoutView(APIView):
    def post(self, request, format=None):
        pass

class RegistrationView(APIView):
    def post(self, request, format=None):
        pass
