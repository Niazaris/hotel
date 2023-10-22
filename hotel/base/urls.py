from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room_listings/', views.room_listings, name='room_listings'),
    path('book_listings/<int:room_id>/', views.book_room, name='book_room'),
    path('contact/', views.contact, name='contact'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('about_us/', views.about_us, name='about_us'),
]