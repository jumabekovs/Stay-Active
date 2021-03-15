import os

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.views import LoginView
from django.dispatch import receiver
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, FormView, UpdateView
from django.views.generic.base import View, TemplateView

from applications.user.forms import RegistrationForm, UserForm, ProfileForm, UpdateProfileForm
from applications.user.models import User
from applications.user.utils import send_activation_code


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form.save()
            return render(self.request, 'accounts/successfully_registered.html', self.get_context_data())
        return render(self.request, 'accounts/registration.html', self.get_context_data())


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



def profile_view(request):
    user = request.user
    form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', locals())


class EditProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = ProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', locals())

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            update = form.save(commit=False)
            update.user = user
            update.save()
            if request.FILES.get('photo', None) is not None:
                try:
                    os.remove(request.user.get_image_url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                request.user.photo = request.FILES['photo']
                request.user.save()
            return redirect('profile')
        else:
            return ProfileForm(instance=request.user)





