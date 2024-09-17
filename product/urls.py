from django.urls import path
from .views import product_list, create_product, index

urlpatterns = [
    path('', index),
    path('product/', product_list),
    path('product/create/', create_product),
]
