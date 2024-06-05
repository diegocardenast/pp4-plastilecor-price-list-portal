from .models import ContactUsRequest
from django import forms

"""Form class used inside the contact page"""
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsRequest
        fields = ('name', 'email', 'message')
