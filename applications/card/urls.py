from django.urls import path
from .views import *

urlpatterns = [
    path('offers/', CardsView.as_view(), name='cards'),
]