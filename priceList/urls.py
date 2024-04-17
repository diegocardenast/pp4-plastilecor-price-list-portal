from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='priceL'),
    path('<productCode>/', views.product_detail, name='product_detail'),
]