from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER


def send_activation_code(user):
    user.create_activation_code()
    message = f"""Thank you, for your registration. To activate your account
                please follow the link below:    
                
                http://127.0.0.1:8000/accounts/activation/?token={user.activation_code}"""
    send_mail(
        'Account activation', message,
        EMAIL_HOST_USER,
        [user.email, ])


