from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import ListItem
from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from .forms import ProductForm
from django.contrib.auth.models import User

class PostList(generic.ListView):
    """ View all products """
    queryset = ListItem.objects.all()
    template_name = "priceList/index.html"
    paginate_by = 6


def product_detail(request, productCode):
    """ Display an individual product """

    productDetail = get_object_or_404(ListItem, productCode=productCode)

    return render(
        request,
        "priceList/product_detail.html",
        {"product": productDetail},
    )

class AddProduct(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Add product"""

    template_name = "priceList/add_product.html"
    model = ListItem
    form_class = ProductForm
    success_url = reverse_lazy('priceL')
    success_message = "Product successfully created!"

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(AddProduct, self).form_valid(form)


class EditProduct(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a product"""
    template_name = 'priceList/edit_product.html'
    model = ListItem
    form_class = ProductForm
    success_url = reverse_lazy('priceL')
    success_message = "Product successfully updated!"
    
    def test_func(self):
        list_item = self.get_object()
        
        return self.request.user == list_item.author


class DeleteProduct(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    """Delete a product"""
    template_name = 'priceList/product_confirm_delete.html' 
    model = ListItem 
    success_url = reverse_lazy('priceL')
    success_message = "Product successfully deleted!"
    
    def test_func(self):
        list_item = self.get_object()
        
        return self.request.user == list_item.author