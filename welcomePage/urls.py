from . import views
from django.urls import path

"""Path to welcome page"""
urlpatterns = [
    path('', views.welcome_me, name='welcome'),
]
