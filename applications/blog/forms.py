from django import forms
from django.core.mail import send_mail

from project.settings import EMAIL_HOST_USER


class SendWishesForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=True, max_length=1000)

    def send_wishes(self):
        data = self.cleaned_data
        message = data.get('message')
        subject = data.get('subject')
        email = data.get('email')
        message_ = f' User with email {email} thinks about {subject}, and wants to add {message}'
        send_mail(subject, message_, EMAIL_HOST_USER, ['azamatjumma@gmail.com', ])