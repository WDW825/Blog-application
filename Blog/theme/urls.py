from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.theme_create, name='theme_create'),
    path('<str:theme_name>/', views.theme_home, name='theme_home')
]

