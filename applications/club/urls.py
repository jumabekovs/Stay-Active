from django.urls import path
from .views import ClubView, ClubDetailView, ClubCategoryDetailView

urlpatterns = [
    path('clubs/', ClubView.as_view(), name='clubs'),
    path('clubs/<str:slug>/', ClubDetailView.as_view(), name='club-detail'),
    path('<str:slug>/', ClubCategoryDetailView.as_view(), name='clubs-category'),

]
