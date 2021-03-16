import os
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View

from applications.user.forms import RegistrationForm, ProfileForm
from applications.user.models import User


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
                    print(_('Exception in removing old profile image: '), e)
                request.user.photo = request.FILES['photo']
                request.user.save()
            return redirect('profile')
        else:
            return ProfileForm(instance=request.user)





