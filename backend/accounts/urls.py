from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='log in view'),
    path('logout/', views.LogoutView.as_view(), name='log out view'),
    path('register/', views.RegistrationView.as_view(), name='registration view'),
    path('<str:username>/', views.ProfilePageView.as_view(), name='profile page view'),
]