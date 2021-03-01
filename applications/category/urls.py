from django.urls import path
from .views import ClubCategoryDetailView, PostCategoryDetailView

urlpatterns = [
    path('<str:slug>/', ClubCategoryDetailView.as_view(), name='clubs-category'),
    path('blog/<str:slug>/', PostCategoryDetailView.as_view(), name='category-post'),

]
