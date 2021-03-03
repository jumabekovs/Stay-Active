from django import forms

from django.contrib.auth import get_user_model
from .utils import send_activation_code

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation', 'age', 'gender', 'photo')