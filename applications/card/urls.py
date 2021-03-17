from django.urls import path
from .views import *

urlpatterns = [
    path('', CardsView.as_view(), name='cards'),
    path('add/<int:pk>/', get_card, name='get_card')
]