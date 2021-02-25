from django.views.generic import ListView

from .models import Offer


class CardsView(ListView):
    model = Offer
    template_name = 'cards.html'
    context_object_name = 'cards'