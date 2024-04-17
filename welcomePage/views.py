from django.shortcuts import render
from .models import WelcomePage

# Create your views here.
def welcome_me(request):
    """
    Renders the Welcome-Home page
    """
    welcome = WelcomePage.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "welcomePage/welcome.html",
        {"welcome": welcome},
    )