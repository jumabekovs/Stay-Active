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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email is already exists!')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Passwords did not match')
        return data


    def save(self, commit=True):
        user = User.objects.create(**self.cleaned_data)
        send_activation_code(user)
        return user
