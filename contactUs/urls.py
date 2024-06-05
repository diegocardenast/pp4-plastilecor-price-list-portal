from . import views
from django.urls import path

"""Contact form URL"""
urlpatterns = [
    path('', views.contact_us, name='contact_form'),
]