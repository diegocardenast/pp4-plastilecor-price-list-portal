from . import views
from django.urls import path
from .views import (
    DeleteProduct, EditProduct, AddProduct,
)

urlpatterns = [
    path('', views.PostList.as_view(), name='priceL'),
    path("add/", AddProduct.as_view(), name='add_product'),
    path('<productCode>/', views.product_detail, name='product_detail'),
    path("delete/<int:pk>/", DeleteProduct.as_view(), name="delete_product"),
    path("edit/<int:pk>/", EditProduct.as_view(), name="edit_product"),
]
