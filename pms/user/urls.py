from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
# from django.contrib.auth.views import LogoutView
urlpatterns = [
 
 path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
 path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
 path('login/',UserLoginView.as_view(),name='login'),
 path('logout/',UserLogoutView.as_view(),name='logout'),
 path('signup/',SignUpView.as_view(),name='signup'),
 path('dashboard/',views.dashboard,name='dashboard'),
 path('password/',views.password,name='password'),
 path('navbar/',views.navbar,name='navbar'),
]