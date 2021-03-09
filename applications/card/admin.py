from django.contrib import admin

from .models import Card, Order

admin.site.register(Card)
admin.site.register(Order)