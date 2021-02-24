from django.urls import path
from .views import club

urlpatterns = [
    path('clubs/', club, name='clubs'),

]