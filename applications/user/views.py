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




# class ProfileView(DetailView):
#     model = User
#     template_name = 'accounts/profile.html'
#
#     def get_object(self):
#         return get_object_or_404(User, email=self.kwargs.get('email'))
#
#     def get_context_data(self, **kwargs):
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         print(context)



def profile_view(request):
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
            return redirect('profile')
        else:
            return ProfileForm(instance=request.user)




