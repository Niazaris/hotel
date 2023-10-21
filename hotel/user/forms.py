from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.forms import DateTimeInput
from django.utils.translation import gettext_lazy as _