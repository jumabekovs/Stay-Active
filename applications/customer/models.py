from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


GENDER_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('NS', _('Not Specified')),
)


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, blank=True, null=True, help_text=_('Contact phone number'))
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='NS')
    photo = models.ImageField(default=" default_profile.png", null=True, blank=True, upload_to='profile_images')
    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now)
    objects = CustomUserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email