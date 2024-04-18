from .models import ContactUsRequest
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsRequest
        fields = ('name', 'email', 'message')