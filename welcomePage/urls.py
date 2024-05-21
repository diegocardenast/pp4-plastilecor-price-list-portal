from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome_me, name='welcome'),
]
