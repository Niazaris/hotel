from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from .models import Room, Booking
from .forms import BookingForm

def home(request):
    return render(request, 'base/home.html')

def room_listings(request):
    rooms = Room.objects.all()
    return render(request, 'base/room_listings.html', {'rooms': rooms})

def contact(request):
    return render(request, 'base/contact.html')

def about_us(request):
    return render(request, 'base/about_us.html')

def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            try:
                booking.save()
            except ValidationError as e:
                error_message = str(e)
                return HttpResponse(f"Error: {error_message}")         
            return redirect('booking_success') 
    else:
        form = BookingForm()

    return render(request, 'base/booking.html', {'form': form, 'room': room})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('profile')

def booking_success(request):
    return render(request, 'base/booking_success.html')