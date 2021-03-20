from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.category.models import CategoryClub

GENDER_SEGREGATION = (
    ('men', _('Only for Men')),
    ('women', _('Only for Women')),
    ('both', _('Open')),
)


class Club(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=255)
    type_category = models.ManyToManyField(CategoryClub, related_name='club_types', verbose_name='club_types')
    gender_segregation = models.CharField(max_length=25, choices=GENDER_SEGREGATION)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(max_length=14, blank=True, help_text=_('Contact phone number'))
    area = models.IntegerField()
    address = models.CharField(max_length=400, unique=True, blank=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='classes-1.jpg', upload_to='club_images', blank=True, null=True)

    def __str__(self):
        return f'{self.name} -{self.type_category.all()}'

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''  # if no image, return empty string


class ClubImage(models.Model):
    images = models.FileField(default='default_club_logo.jpg', upload_to='club_images', blank=True, null=True)
    club = models.ForeignKey(Club, related_name='images', on_delete=models.CASCADE)

    def get_image_url(self):
        if self.images:
            return self.images.url
        return ''
