import uuid
from datetime import timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.category.models import CategoryOffer
from applications.user.forms import User

OFFER_DURATION = (
    ('30', _('30 days')),
    ('90', _('90 days')),
)



class Card(models.Model):
    type = models.ForeignKey(CategoryOffer, on_delete=models.DO_NOTHING, related_name='offers')
    duration = models.CharField(max_length=55, choices=OFFER_DURATION)
    price = models.CharField(max_length=15)
    description = models.TextField()


    def __str__(self):
        return f'{self.type}-{self.duration}-{self.price}'



class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='orders', blank=True)
    card = models.ForeignKey(Card, null=True, on_delete=models.CASCADE, related_name='card_orders')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    activation_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def save(self):
        d = timedelta(days=int(self.card.duration))

        if self.activation_date is not None:
            self.expire_date = self.activation_date + d
            self.status = True
            super(Offer, self).save()
        else:
            self.expire_date = None
            super(Offer, self).save()

    def __str__(self):
        return self.client.email




