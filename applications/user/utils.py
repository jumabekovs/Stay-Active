from django.core.mail import send_mail


def send_activation_code(user):
    user.create_activation_code()
    message = f"""Thank you, for your registration. To activate your account'
                follow link:http://127.0.0.1:8000/accounts/activation/?u={user.activation_code}"""
    send_mail(
        'Account activation', message,
        'test@my_project.com',
        [user.email, ])



