from django.contrib.auth.views import LogoutView
from django.urls import path

from .recaptcha import check_recaptcha
from .views import *

urlpatterns = [
    path('register/', check_recaptcha(RegistrationView.as_view()), name='registration'),
    path('successful-registration/', SuccessfulRegistrationView.as_view(), name='successfully-registered'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
]