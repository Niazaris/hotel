from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room_listings/', views.room_listings, name='room_listings'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_us, name='about_us'),
]