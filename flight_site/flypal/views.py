from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return render(request, 'flypal/home_page.html')


def login_view(request):
    return render(request, 'flypal/login.html')


def register_view(request):
    return render(request, 'flypal/register.html')