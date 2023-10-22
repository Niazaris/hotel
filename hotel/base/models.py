from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

User = get_user_model()

def validate_room_image(value):
    if not value:
        raise ValidationError("Image is required for a room.")

class Room(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    beds_number = models.PositiveSmallIntegerField()
    room_number = models.PositiveIntegerField(unique=True)
    is_available = models.BooleanField(default=True)
    room_image = models.ImageField(upload_to='room_images/', null=True, blank=True, validators=[validate_room_image])
    notes  = models.TextField(max_length=500, null=True, blank=True)


    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")


    def save(self, *args, **kwargs):
        today = date.today()
        if self.check_in_date < today:
            raise ValidationError(_("Check in date cannot be earlier than today."))
        elif self.check_out_date < self.check_in_date:
            raise ValidationError(_("Check out date cannot be earlier than Check in."))
        elif self.check_in_date  > self.check_out_date:
            raise ValidationError(_("Check in  date cannot be later than Check out."))
        elif self.check_in_date  == self.check_out_date:
             raise ValidationError(_("Check in  and Check out can not be the same."))
        else:
            self.room.is_available = False
            self.room.save()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.room.is_available = True
        self.room.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.room} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})