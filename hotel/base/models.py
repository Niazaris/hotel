from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import uuid

User = get_user_model()

ROOM_STATUS = (
    (0, _("available")),
    (1, _("booked")),
    (2, _("unavailable")),
)

def validate_room_image(value):
    if not value:
        raise ValidationError("Image is required for a room.")

class Room(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    beds_number = models.PositiveSmallIntegerField()
    room_number = models.PositiveIntegerField(unique=True)
    room_image = models.ImageField(upload_to='room_images/', null=True, blank=True, validators=[validate_room_image])
    notes  = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Reservation(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100)
    booked_room_number = models.ForeignKey(
        Room, 
        verbose_name=_("reservation"),
        on_delete=models.CASCADE,
        related_name="reservetion",
    )
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    notes  = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = _("reservation")
        verbose_name_plural = _("reservations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class RoomInstance(models.Model):
    unique_id = models.UUIDField(
        _("unique ID"), 
        db_index=True, 
        unique=True,
        default=uuid.uuid4,
    )

    room = models.ForeignKey(
        Room, 
        verbose_name=_("room"),
        related_name="instances",
        on_delete=models.CASCADE,
    )

    status = models.PositiveSmallIntegerField(
        _("status"), choices=ROOM_STATUS, default=0
    )

    class Meta:
        verbose_name = _("Room instance")
        verbose_name_plural = _("Room instances")

    def __str__(self):
        return f"UUID:{self.unique_id}, {self.room}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})