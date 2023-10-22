from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'beds_number', 'room_number', 'price')
    search_fields = ('name', 'beds_number', 'room_number', 'price')
    
admin.site.register(models.Booking)

