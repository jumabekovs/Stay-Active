from datetime import date


from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.utils.translation import ugettext_lazy as _

from applications.user.managers import CustomUserManager


GENDER_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('NS', _('Not Specified')),
)


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(default=date.today, blank=True)
    phone = models.CharField(max_length=14, blank=True, null=True, help_text=_('Contact phone number'))
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='NS')
    photo = models.ImageField(default="default_profile.png", upload_to='profile_images')
    card_purchased = models.BooleanField(default=False)
    objects = CustomUserManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    activation_code = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_staff

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(15)
        if User.objects.filter(activation_code=code).exists():
            self.create_activation_code()
        self.activation_code = code
        self.save(update_fields=['activation_code'])

    def get_image_url(self):
        if self.photo:
            return self.photo.url
        return ''


    def calculate_age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

