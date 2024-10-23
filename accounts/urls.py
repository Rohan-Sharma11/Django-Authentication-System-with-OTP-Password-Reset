# accounts/urls.py

from django.urls import path
from . import views
from .views import signup_view, login_view, forgot_password_view, reset_password_view, logout_view

from django.shortcuts import redirect

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
]
