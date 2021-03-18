from django.contrib import messages
from django.db import IntegrityError

from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Card, Offer, OfferHistory


class CardsView(ListView):
    model = Card
    template_name = 'applications/cards.html'
    context_object_name = 'cards'


class AddCardToProfile(View):

    def get(self, request, *args, **kwargs):
        try:
            card_id = kwargs.get('pk')
            user = request.user
            card = Card.objects.get(pk=card_id)
            Offer.objects.get_or_create(client=user, card=card, paid=True)
            OfferHistory.objects.get_or_create(client=user, card=card, paid=True)
            messages.add_message(request, messages.INFO, 'You purchased a card')
            return redirect('profile')
        except IntegrityError:
            messages.add_message(request, messages.INFO, 'You can not purchase second card, first you have delete one')
            return redirect('profile')


class RemoveCardToProfile(View):

    def get(self, request, *args, **kwargs):
        offer_id = kwargs.get('pk')
        print(offer_id)
        offer = Offer.objects.get(pk=offer_id)
        print(offer)
        offer.delete()
        messages.add_message(request, messages.INFO, 'You card has been removed!')
        return redirect('profile')
