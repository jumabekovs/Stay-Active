from django.contrib import admin

from applications.blog.models import Post, ExtendPost, AuthorPost


class ExtendPostInline(admin.TabularInline):
    model = ExtendPost
    max_num = 5
    extra = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [ExtendPostInline, ]


admin.site.register(Post, PostAdmin)
admin.site.register(AuthorPost)
