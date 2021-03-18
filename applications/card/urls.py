from django.urls import path
from .views import *

urlpatterns = [
    path('', CardsView.as_view(), name='cards'),
    path('add/<int:pk>/', AddCardToProfile.as_view(), name='get_card'),
    path('remove/<str:pk>/', RemoveCardToProfile.as_view(), name='remove_card'),
]