# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['from_email'].label = "Your email:"
    self.fields['subject'].label = "subject:"
    self.fields['content'].label = "What do you want to say?"
