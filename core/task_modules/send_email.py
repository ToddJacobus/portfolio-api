import os
from django.core.mail import send_mail

def send_email_to_me(*args, **kwargs):
    name = kwargs.get('name')
    email = kwargs.get('email')
    comments = kwargs.get('comments')

    send_mail(
        subject=f'ToddJacobus.io -- {name}',
        from_email={email},
        message=f"{email}\n\n{comments}",
        recipient_list = [
            "rtjacobus1@gmail.com",
        ],
        fail_silently=False,
    )