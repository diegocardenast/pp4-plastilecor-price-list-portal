from django.shortcuts import render, get_object_or_404 
# from django.http import HttpResponse -- NOT NEEDED AFTER CREATING THE VIEWS
from django.views import generic
from .models import ListItem


#def my_priceList(request):
#    return HttpResponse("Hello, Plastilecor!")  -- NOT NEEDED AFTER CREATING THE VIEWS

# Create your views here.

class PostList(generic.ListView):
    queryset = ListItem.objects.all()
    # template_name = "priceList/price_list.html" -- NOT NEEDED AFTER CREATING INDEX.html
    template_name = "priceList/index.html"
    paginate_by = 6


def product_detail(request, productCode):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    productDetail = get_object_or_404(ListItem, productCode=productCode)

    return render(
        request,
        "priceList/product_detail.html",
        {"product": productDetail},
    )