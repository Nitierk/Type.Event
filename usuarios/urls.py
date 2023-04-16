from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
]