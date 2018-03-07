# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            # TEST
            template = get_template('contact_template.txt')
            context = {
                'subject': subject,
                'from_email': from_email,
                'message': message,
            }
            content = template.render(context)
            # content = get_template('contact_template.txt').render(context)

            try:
                email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + '',
                    ['youremail@gmail.com'],
                    headers={'Reply-To': from_email}
                )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('sendemail:success')
            # END TEST

            """try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('success')
            return redirect('sendemail:success')"""
    return render(request, "email.html", {'form': form})


def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    return render(request, template_name="success.html")
