from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import *



class ClubView(ListView):
    model = Club
    template_name = 'clubs.html'
    context_object_name = 'clubs'
    ordering = ['type']



class ClubDetailView(DetailView):
    model = Club
    template_name = 'club_detail.html'
    context_object_name = 'club'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.get_object().images.all()
        return context



