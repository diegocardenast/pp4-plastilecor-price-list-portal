"""
URL configuration for plastilecor_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from priceList import views as priceList_views -- NOT NEEDED AFTER CREATION OF URLS FOR ALL THE APP

urlpatterns = [
    #path("priceList/", priceList_views.my_priceList, name='myPriceList'),  -- NOT NEEDED AFTER CREATION OF URLS FOR ALL THE APP
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('contactUs/', include("contactUs.urls"), name="contactUs-urls"),
    path('priceList/', include("priceList.urls"), name="priceList-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("welcomePage.urls"), name="welcomePage-urls"),
    
]
