from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.theme_feed, name='theme_feed'),
    path('create/', views.theme_create, name='theme_create'),
    path('<str:theme_name>/', views.theme_home, name='theme_home'),
    path('<str:theme_name>/create_post/', views.post_form, name='create_post'),
]

