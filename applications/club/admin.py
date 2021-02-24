from django.contrib import admin
from .models import ClubImage, Club


class ClubImageAdmin(admin.TabularInline):
    model = ClubImage
    max_num = 5
    extra = 0


class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubImageAdmin, ]


admin.site.register(Club, ClubAdmin)
