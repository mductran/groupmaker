from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExampleView, name='log in view'),
]