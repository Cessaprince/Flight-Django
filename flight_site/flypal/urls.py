"""Urls for flypal app"""

from django.urls import path
from . import views

urlpatterns = [
    path('home_page/', views.home_page_view, name='home_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('auth_home_page/', views.auth_home_page_view, name='auth_home_page'),
    path('flight_results/<str:flying_from>/<str:flying_to>/<str:departing>/<str:returning>/<str:adults>/<str:children>/<str:flight_choice>/', 
        views.flight_results, name='flight_results'),
]