from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.views import LoginView
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView
from django.views.generic.base import View, TemplateView

from applications.user.forms import RegistrationForm
from applications.user.models import User
from applications.user.utils import send_activation_code


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('successfully-registered')


class SuccessfulRegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/successfully_registered.html', {})


class ActivationView(View):
    def get(self, request):
        code = request.GET.get('token')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'accounts/activation.html', {})


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    success_url = reverse_lazy('home')




def ProfilePage(request):
    return render(request, 'accounts/user.html', locals())
