from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *



class ClubView(ListView):
    model = Club
    template_name = 'clubs.html'
    context_object_name = 'club_types'
    ordering = ['type']


class ClubDetailView(DetailView):
    model = Club
    template_name = 'club_detail.html'
    context_object_name = 'club_types'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.get_object().images.all()
        return context


# def club_category(request, type):
#     clubs = Club.objects.all().filter(type=type)
#     return render(request, 'clubs.html', locals())


class ClubCategoryDetailView(DetailView):
    model = CategoryClub
    template_name = 'clubs.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club_types'] = self.get_object().club_types.all()
        return context