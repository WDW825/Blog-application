from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('create_post/', views.post_form, name='create_post'),
    path('login/', include('login.urls'))
]
