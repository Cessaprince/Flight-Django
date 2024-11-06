"""Urls for flypal app"""

from django.urls import path
from . import views

urlpatterns = [
    path('home_page/', views.home_page_view, name='home_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('auth_home_page/', views.auth_home_page_view, name='auth_home_page')
]