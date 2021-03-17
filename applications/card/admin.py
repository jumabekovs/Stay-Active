from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Card, Offer


class CardAdmin(TranslationAdmin):
    list_display = ('type', 'duration', 'description', 'price')
    list_display_links = ('type',)
    list_filter = ('duration',)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('client', 'status')
    list_display_links = ('client',)
    list_filter = ('status',)
    search_fields = ('client',)
    ordering = ('-date_created',)


admin.site.register(Card, CardAdmin)
admin.site.register(Offer, OfferAdmin)