from django import forms
from crispy_forms.helper import FormHelper


class NewsletterUserSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels=False

    class Meta:
        model = NewsletterUserSignUpFormfield = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email


# Test

# from invoices.models import Customer
class InvoiceForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
    )
    number = forms.CharField(label='Invoice #')
    # customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    subject = forms.CharField()
    amount = forms.DecimalField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)

# End Test