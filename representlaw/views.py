from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives


def login_redirect(request):
    return redirect('/website/login')