from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def room_listings(request):
    return render(request, 'base/room_listings.html')

def contact(request):
    return render(request, 'base/contact.html')

def about_us(request):
    return render(request, 'base/about_us.html')