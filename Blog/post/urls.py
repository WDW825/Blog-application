from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create_post/', views.post_form, name='create_post'),
    path('edit_post/', views.edit_post, name='edit_post')
]


#TODO: make redirect from '' to 'create_post/'