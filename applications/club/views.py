from django.shortcuts import render
from django.views.generic import ListView

from .models import *



class ClubView(ListView):
    model = Club
    template_name = 'clubs.html'
    context_object_name = 'clubs'
    ordering = ['type']