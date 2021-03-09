from django.views.generic import ListView

from .models import Card


class CardsView(ListView):
    model = Card
    template_name = 'cards.html'
    context_object_name = 'cards'