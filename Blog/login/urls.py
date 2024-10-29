from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='reg')
]