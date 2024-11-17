from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('edit_post/', views.edit_post, name='edit_post'),
]
