from modeltranslation.translator import translator, TranslationOptions
from .models import Club


class ClubTranslationOptions(TranslationOptions):
    fields = ('address', 'description')


translator.register(Club, ClubTranslationOptions)