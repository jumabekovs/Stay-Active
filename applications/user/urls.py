from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
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
    path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

]
