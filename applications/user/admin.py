from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'name', 'last_name', 'is_active')
    list_display_links = ('email', 'username', 'name')


admin.site.register(User, UserAdmin)
