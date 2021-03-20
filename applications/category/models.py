from django.db import models
from django.utils.translation import ugettext_lazy as _


TITLE_CHOICES = (
    ('news', _('News')),
    ('diet', _('Diet')),
    ('exercises', _('Exercises')),
    ('life-style', _('Life-Style')),
)
TYPE_CHOICES = (
    ('gym', _('Fitness-Centers')),
    ('pool', _('Pools')),
    ('yoga', _('Yoga-Studios')),
)
OFFER_TYPES = (
    ('comfort', _('Comfort')),
    ('open', _('Open')),
)


class CategoryPost(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children')
    slug = models.SlugField(max_length=100, choices=TITLE_CHOICES, blank=True, primary_key=True)
    title = models.CharField(max_length=60, blank=True)
    logo = models.FileField(upload_to='category_logo', null=True, blank=True)

    class Meta:
        verbose_name = _('Post Category')
        verbose_name_plural = _('Post Categories')

    def __str__(self):
        return f'{self.slug}'

    def get_image_url(self):
        if self.logo:
            return self.logo.url
        return ''


class CategoryClub(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children')
    slug = models.SlugField(max_length=100, choices=TYPE_CHOICES, blank=True, primary_key=True)
    title = models.CharField(max_length=60, blank=True)

    logo = models.FileField(upload_to='category_logo', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Club Category')
        verbose_name_plural = _('Club Categories')

    def __str__(self):
        return f'{self.title}'

    def get_image_url(self):
        if self.logo:
            return self.logo.url
        return ''


class CategoryOffer(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children')
    slug = models.SlugField(max_length=100, choices=OFFER_TYPES, blank=True, primary_key=True)
    title = models.CharField(max_length=60, blank=True)
    logo = models.FileField(upload_to='category_logo', null=True, blank=True)

    class Meta:
        verbose_name = _('Offer Category')
        verbose_name_plural = _('Offer Categories')

    def __str__(self):
        return self.slug

    def get_image_url(self):
        if self.logo:
            return self.logo.url
        return ''






