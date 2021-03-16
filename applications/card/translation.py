from modeltranslation.translator import translator, TranslationOptions
from .models import Card


class CardTranslationOptions(TranslationOptions):
    fields = ('description',)



translator.register(Card, CardTranslationOptions)