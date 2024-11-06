from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'flypal/home_page.html')

from django.http import HttpResponse
from .models import Flight

def auth_home_page_view(request):
    if request.method == 'POST':
        flying_from = request.POST.get('flying_from')
        flying_to = request.POST.get('flying_to_input')
        departing = request.POST.get('departing')
        returning = request.POST.get('returning')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        flight_choice = request.POST.get('f_choice')

        # Query flights based on search criteria
        flights = Flight.objects.filter(
            departure_airport=flying_from,
            arrival_airport=flying_to,
            departure_date=departing,
        )
        if returning:
            flights = flights.filter(return_date=returning)

        # Redirect to flight results page
        return redirect('flight_results', flying_from, flying_to, departing, returning, adults, children, flight_choice)

    else:
        return render(request, 'flypal/auth_home_page.html')
    
def flight_results(request, flying_from, flying_to, departing, returning, adults, children, flight_choice):
    flights = Flight.objects.filter(
        departure_airport=flying_from,
        arrival_airport=flying_to,
        departure_date=departing,
        adult_passenger= adults,
        children_passenger = children,
        flight_choice=flight_choice
    )
    if returning:
        flights = flights.filter(return_date=returning)

    return render(request, 'flypal/flight_results.html', {'flights': flights})


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