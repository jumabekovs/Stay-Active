from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import OfferForm
from .models import Card, Offer
from ..user.models import User


class CardsView(ListView):
    model = Card
    template_name = 'applications/cards.html'
    context_object_name = 'cards'


def get_card(request, pk):
    user = request.user
    card = Card.objects.get(pk=pk)
    Offer.objects.get_or_create(client=user, card=card, paid=True)
    messages.add_message(request, messages.INFO, 'You purchased a card')
    return redirect('profile')

