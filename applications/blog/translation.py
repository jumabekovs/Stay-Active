from modeltranslation.translator import translator, TranslationOptions
from .models import Post, ExtendPost, AuthorPost


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'content')


class ExtendPostTranslationOptions(TranslationOptions):
    fields = ('header', 'text')


class AuthorTranslationOptions(TranslationOptions):
    fields = ('short_intro',)


translator.register(Post, PostTranslationOptions)
translator.register(ExtendPost, ExtendPostTranslationOptions)
translator.register(AuthorPost, AuthorTranslationOptions)