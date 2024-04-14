from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<productCode>/', views.product_detail, name='product_detail'),
]