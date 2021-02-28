from django.urls import path
from .views import ClubCategoryDetailView

urlpatterns = [
    path('<str:slug>/', ClubCategoryDetailView.as_view(), name='clubs-category'),

]
