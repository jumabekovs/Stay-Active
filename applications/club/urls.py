from django.urls import path
from .views import ClubView, ClubDetailView

urlpatterns = [
    path('', ClubView.as_view(), name='clubs'),
    path('<str:slug>/', ClubDetailView.as_view(), name='club-detail'),

]
