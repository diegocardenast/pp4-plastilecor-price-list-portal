from django.shortcuts import render
from .models import ContactUsRequest
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    contact_form = ContactForm()

    return render(
        request,
        "contactUs/contact.html",
        {
            "contact_form": contact_form
        },
    )
