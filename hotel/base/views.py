from django.shortcuts import render
from .models import Room

def home(request):
    return render(request, 'base/home.html')

def room_listings(request):
    rooms = Room.objects.all()
    return render(request, 'base/room_listings.html', {'rooms': rooms})

def contact(request):
    return render(request, 'base/contact.html')

def about_us(request):
    return render(request, 'base/about_us.html')