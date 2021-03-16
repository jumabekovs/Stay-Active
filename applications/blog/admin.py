from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from applications.blog.models import Post, ExtendPost, AuthorPost


class ExtendPostInline(admin.TabularInline):
    model = ExtendPost
    max_num = 5
    extra = 2


class PostAdmin(TranslationAdmin):
    list_display = ('title', 'blogger')
    inlines = [ExtendPostInline, ]
    search_fields = ('title',)
    list_display_links = ('blogger',)


admin.site.register(Post, PostAdmin)
admin.site.register(AuthorPost)
