from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryPost, CategoryClub, CategoryOffer


class CategoryPostTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryOfferTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryClubTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(CategoryPost, CategoryPostTranslationOptions)
translator.register(CategoryOffer, CategoryOfferTranslationOptions)
translator.register(CategoryClub, CategoryClubTranslationOptions)