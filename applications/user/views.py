from django.shortcuts import render
from django.views.generic import CreateView

from applications.customer.models import User


class RegistrationView(CreateView):
    model = User
    template_name = 'account/registration.html'
