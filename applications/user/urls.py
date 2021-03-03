from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('successful_registration/', SuccessfulRegistrationView.as_view(), name='successfully-registered'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('log-out/', LogoutView.as_view(), name='logout'),
]