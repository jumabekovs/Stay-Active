from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import *



class ClubView(ListView):
    model = Club
    template_name = 'clubs.html'
    context_object_name = 'clubs'
    ordering = ['type']

    def get_template_names(self):
        template_name = super(ClubView, self).get_template_names()
        search = self.request.GET.get('search')
        if search:
            template_name = 'search.html'
        return template_name


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        gender = self.request.GET.get('filter')
        print(filter)
        if search:
            context['clubs'] = Club.objects.filter(Q(name__icontains=search) | Q(slug__icontains=search))

        elif gender == 'men':
            context['clubs'] = Club.objects.filter(gender_segregation='men')
        elif gender == 'women':
            context['clubs'] = Club.objects.filter(gender_segregation='women')
        elif gender == 'both':
            context['clubs'] = Club.objects.filter(gender_segregation='both')
        else:
            context['clubs'] = Club.objects.all()
        return context




class ClubDetailView(DetailView):
    model = Club
    template_name = 'club_detail.html'
    context_object_name = 'club'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.get_object().images.all()
        return context



