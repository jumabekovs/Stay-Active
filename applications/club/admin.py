from django.contrib import admin
from .models import ClubImage, Club
from modeltranslation.admin import TranslationAdmin


class ClubImageAdmin(admin.TabularInline):
    model = ClubImage
    max_num = 5
    extra = 0


class ClubAdmin(TranslationAdmin):
    inlines = [ClubImageAdmin, ]


admin.site.register(Club, ClubAdmin)
