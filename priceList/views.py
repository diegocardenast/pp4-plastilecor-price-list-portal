from django.shortcuts import render
# from django.http import HttpResponse -- NOT NEEDED AFTER CREATING THE VIEWS
from django.views import generic
from .models import ListItem



#def my_priceList(request):
#    return HttpResponse("Hello, Plastilecor!")  -- NOT NEEDED AFTER CREATING THE VIEWS

# Create your views here.

class PostList(generic.ListView):
    queryset = ListItem.objects.all()
    template_name = "priceList/price_list.html"