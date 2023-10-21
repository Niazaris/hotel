from datetime import date
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

class Room(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.PositiveIntegerField()
    beds_number = models.PositiveSmallIntegerField()
    room_number = models.PositiveIntegerField()
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
    star_date = models.DateField
    end_date = models.DateField
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
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})