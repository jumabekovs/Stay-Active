from django.forms import ModelForm
from django import forms
from applications.card.models import Offer



class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'



