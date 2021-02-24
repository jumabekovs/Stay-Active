from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.category.models import CategoryOffer

OFFER_DURATION = (
    ('1 MONTH', _('1 месяц')),
    ('3 MONTHS', _('3 месяца')),
)


class Offer(models.Model):
    type = models.ForeignKey(CategoryOffer, on_delete=models.DO_NOTHING, related_name='offers')
    duration = models.CharField(max_length=55, choices=OFFER_DURATION)
    price = models.CharField(max_length=15)
    description = models.TextField()
    activation_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.type}-{self.duration}-{self.price}'
