from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout, decorators
from django.utils.decorators import method_decorator


from .models import Users


class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # redirect to last visited page
            pass
        else:
            error = {"AuthenticationError": "Invalid username or password"}
            return Response(data=error, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request, format=None):
        logout(request)


class RegistrationView(APIView):
    def post(self, request, format=None):
        pass


@method_decorator(decorators.login_required, name="dispatch")
class ProfilePageView(APIView):
    def get(self, request, username, format=None):
        user = Users.objects.get(username=username)
        if user is not None:
            pass
        else:
            return

    def put(self, request, username, format=None):
        pass

    def delete(self, request, username, format=None):
        pass


@method_decorator(decorators.login_required, name="dispatch")
class UserPostView(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass


@method_decorator(decorators.login_required, name="dispatch")
class UserGroupView(APIView):
    pass


@method_decorator(decorators.login_required, name="dispatch")
class UserMessageView(APIView):
    pass


@method_decorator(decorators.login_required, name="dispatch")
class UserTaskView(APIView):
    pass


@method_decorator(decorators.login_required, name="dispatch")
class UserReviewView(APIView):
    pass
