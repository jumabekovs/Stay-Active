from django.urls import path
from .views import ClubView, ClubDetailView, ClubCategoryDetailView

urlpatterns = [
    path('clubs/', ClubView.as_view(), name='clubs'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),
    path('clubs/<str:slug>/', ClubCategoryDetailView.as_view(), name='clubs-category'),

]