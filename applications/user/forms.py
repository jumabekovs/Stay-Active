from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .utils import send_activation_code

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (_('username'), _('email'), _('name'), _('last_name'), _('birthday'), _('phone'), _('gender'), _('photo'), )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (_('username'), _('email'), _('name'), _('last_name'), _('birthday'), _('phone'), _('gender'), _('photo'), )




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (_('email'), _('password'), _('password_confirmation'), _('birthday'), _('gender'), _('photo'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('User with this email is already exists!'))
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError(_('Passwords did not match'))
        return data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.is_active = False    # deactivating user
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            send_activation_code(user)
        return user




class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birthday = forms.DateField(required=False)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (_('username'), _('email'), _('name'), _('last_name'), _('birthday'), _('phone'), _('gender'), _('photo'), )


    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(_('This email address is already in use. Please supply a different email address.'))
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user