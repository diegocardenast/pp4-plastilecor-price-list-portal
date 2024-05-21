from django.shortcuts import render
from django.contrib import messages
from .models import ContactUsRequest
from .forms import ContactForm

# Create your views here.


def contact_us(request):
    # POST handling.
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Request received! We will be in contact with you as soon as we can."
            )

    contact_form = ContactForm()

    return render(
        request,
        "contactUs/contact.html",
        {
            "contact_form": contact_form
        },
    )
