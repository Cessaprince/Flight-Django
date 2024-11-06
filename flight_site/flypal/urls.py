"""Urls for flypal app"""

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page_view, name='home')
]