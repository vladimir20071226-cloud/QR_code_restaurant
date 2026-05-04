"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import menu.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('auth/google/', views.google_auth, name='google_auth'),
    path('auth/google/callback', views.google_callback, name='google_callback'),
    path('menu/all/', views.dish_detail, name='dish_detail'),
    path('menu/<int:pk>', views.menu_detail, name='menu_detail'),
    path('delete/<int:pk>', views.dish_delete, name='dish_delete'),
    path('update/<int:pk>', views.UpdateDish.as_view(), name='dish_update'),
    path('create/', views.CreateDish.as_view(), name='dish_create'),
]
