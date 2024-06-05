from django.contrib import admin
from django.urls import path, include
"""url patterns for Plastilecor portal"""
urlpatterns = [

    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('contactUs/', include("contactUs.urls"), name="contactUs-urls"),
    path('priceList/', include("priceList.urls"), name="priceList-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("welcomePage.urls"), name="welcomePage-urls"),
]
