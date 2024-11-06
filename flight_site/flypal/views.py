from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'flypal/home_page.html')

def auth_home_page_view(request):
    return render(request, 'flypal/auth_home_page.html')

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
        return redirect('auth_home_page')
    return render(request, 'flypal/login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(email=email, password=password1)
            user.save()
            return redirect('login')
    return render(request, 'flypal/register.html')