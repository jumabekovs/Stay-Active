from django.contrib import admin
from .models import CategoryPost, CategoryClub, CategoryOffer
from modeltranslation.admin import TranslationAdmin


class CategoryPostAdmin(TranslationAdmin):
    list_display = ('slug', 'title',)
    list_filter = ('slug', 'title')
    list_display_links = ('slug',)
    search_fields = ('title',)


class CategoryClubAdmin(TranslationAdmin):
    list_display = ('slug', 'title',)
    list_filter = ('slug', 'title')
    list_display_links = ('slug',)
    search_fields = ('title',)


class CategoryOfferAdmin(TranslationAdmin):
    list_display = ('slug', 'title',)
    list_filter = ('slug', 'title')
    list_display_links = ('slug',)
    search_fields = ('title',)


admin.site.register(CategoryPost, CategoryPostAdmin)
admin.site.register(CategoryClub, CategoryClubAdmin)
admin.site.register(CategoryOffer, CategoryOfferAdmin)


