from allauth.account.models import EmailAddress
from allauth.account.signals import user_signed_up, email_confirmed
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View

from applications.user.forms import RegistrationForm
from applications.user.models import User


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successfully-registered')


class SuccessfulRegistrationView(View):
    def get(self, request):
        return render(request, 'account/successfully_registered.html', {})


class ActivationView(View):
    def get(self, request):
        code = request.GET.get('token')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html', {})


class SignInView(LoginView):
    template_name = 'account/sign_in.html'
    success_url = reverse_lazy('home')




@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):

    user.is_active = False
    user.is_staff = True
    Group.objects.get(name='SurveyManager').user_set.add(user)

    user.save()


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):

    new_email_address = EmailAddress.objects.get(email=email_address)
    user = User.objects.get(new_email_address.user)
    user.is_active = True

    user.save()

