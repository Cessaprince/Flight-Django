# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Flight(models.Model):
    AIRCRAFT_TYPES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First Class', 'First Class'),
    ]

    flight_number = models.CharField(max_length=10, unique=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_flights')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_flights')
    departure_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    aircraft_type = models.CharField(max_length=20, choices=AIRCRAFT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} - {self.departure_airport.name} to {self.arrival_airport.name}"