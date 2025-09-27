from django.shortcuts import render
from .models import Car #This brings the Car Case into views

# Create your views here.
def car_list(request):
    cars = Car.objects.all().order_by('-year')# the minus sign re-orders from newest to oldest
    return render(request, 'car_list.html', {'cars': cars})
