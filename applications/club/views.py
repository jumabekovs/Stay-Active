from django.shortcuts import render
from .models import *


def club(request):
    clubs = Club.objects.all().order_by('type')
    return render(request, 'clubs.html', locals())
