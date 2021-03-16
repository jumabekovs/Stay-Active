from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from django.utils.translation import gettext_lazy as _


def send_activation_code(user):
    user.create_activation_code()
    message = _(f"""Thank you, for your registration. To activate your accounts'
                follow link:http://127.0.0.1:8000/accounts/activation/?token={user.activation_code}""")
    send_mail(
        _('Account activation'), message,
        EMAIL_HOST_USER,
        [user.email, ])



